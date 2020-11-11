from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json, session,abort
from app.Models.gestionar_cursos.calificacion_alumno.CalificacionAlumno_dao import CalificacionAlumno_dao
from app.Models.gestionar_cursos.planificacion_examen.PlanificacionExamen_dao import PlanificacionExamen_dao
from app.rutas.gestionar_cursos.calificacion_alumno.Formulario import Formulario

calif_al = Blueprint('calificacion_alumno', __name__, template_folder='templates')

@calif_al.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo'] not in ('ADMIN', 'PASTOR'):
        abort(403, description="Acceso prohibido")

@calif_al.route('/')
def index():
    calif_dao = CalificacionAlumno_dao()
    data = calif_dao.getLista()
    return render_template('calificacion_alumno/index.html', titulo='Registrar calificaciones', items = data)

@calif_al.route('/lista_alumnos/<int:malla_id>/<int:cur_id>/<int:asi_id>/<int:num_id>/<turno>/<int:per_id>')
def listaAlumnos(malla_id, cur_id, asi_id, num_id, turno, per_id):
    calif_dao = CalificacionAlumno_dao()
    data = calif_dao.getListaAlumnos(malla_id, cur_id, asi_id, num_id, turno)
    if not data:
        flash('No posee lista de alumnos', 'warning')
        return redirect(url_for('calificacion_alumno.index'))
    form = Formulario()
    form.malla_id.data = malla_id
    form.cur_id.data = cur_id
    form.asi_id.data = asi_id
    form.num_id.data = num_id
    form.turno.data = turno
    form.alu_id.data = per_id
    # traer examenes segun parametros
    pe_dao = PlanificacionExamen_dao()
    lista_examenes = pe_dao.getListaExamenesPlanificados(malla_id, cur_id, asi_id, num_id, turno, per_id)
    lista_examenes.insert(0, { 'exa_id':'', 'exa_nombre':'...' })
    #form.examenes.choices = [ (str(item['exa_id']), item['exa_nombre']) for item in lista_examenes ]
    return render_template('calificacion_alumno/lista_alumnos.html', titulo='Formulario Calificaciones', items=data, lista_examenes=lista_examenes, form=form)

@calif_al.route('/anular_examen', methods=['POST'])
def anularExamen():
    malla_id = request.form['malla_id']
    cur_id = request.form['cur_id']
    asi_id = request.form['asi_id']
    num_id = request.form['num_id']
    turno = request.form['turno']
    per_id = request.form['alu_id']
    cbo_examen = request.form['cbo_examen']

    if not cbo_examen:
        flash('Debe escoger un examen para anular', 'warning')
        return redirect(url_for('calificacion_alumno.listaAlumnos', malla_id=malla_id, cur_id=cur_id, asi_id=asi_id, num_id=num_id, turno=turno, per_id=per_id ))

    if per_id and turno and num_id and asi_id and cur_id and malla_id:
        calif_dao = CalificacionAlumno_dao()
        save = calif_dao.anularExamen(cbo_examen, session['usu_id'])
        if save==True:
            flash('Procesado exitoso', 'success')
        else:
            flash('Hubo un problema al intentar anular. Favor contacte al Administrador', 'danger')
        return redirect(url_for('calificacion_alumno.listaAlumnos', malla_id=malla_id, cur_id=cur_id, asi_id=asi_id, num_id=num_id, turno=turno, per_id=per_id ))
    flash('Hubo un problema al validar anular. Favor contacte al Administrador', 'danger')
    return redirect(url_for('calificacion_alumno.listaAlumnos', malla_id=malla_id, cur_id=cur_id, asi_id=asi_id, num_id=num_id, turno=turno, per_id=per_id ))

# Guardar via REST
@calif_al.route('/guardar', methods=['POST'])
def guardar():
    res = None
    planex_id = request.json['planex_id']
    alumno_id = request.json['alumno_id']
    cal_puntaje = int(request.json['cal_puntaje'])
    if  planex_id and alumno_id and cal_puntaje:
        #Volver a validar
        if cal_puntaje < 0:
            flash('No debe ser valor negativo', 'danger')
            res = { 'estado': 'error', 'mensaje': 'No debe ser valor negativo'}
            return jsonify(res)
        if cal_puntaje > 100:
            flash('No debe ser valor tan grande', 'danger')
            res = { 'estado': 'error', 'mensaje': 'No debe ser valor tan grande'}
            return jsonify(res)
        calif_dao = CalificacionAlumno_dao()
        res = calif_dao.guardar(planex_id, alumno_id, cal_puntaje, session['usu_id'])
        if res==True:
            flash('Se proceso correctamente', 'success')
            return jsonify({ 'estado': 'exito', 'mensaje': 'Se proceso correctamente'})
        else:
            flash('No Se proceso correctamente', 'danger')
            res = { 'estado': 'error', 'mensaje': 'No se proceso correctamente'}
    else:
        flash('No Se proceso correctamente', 'danger')
        res = { 'estado': 'error', 'mensaje': 'No se ha enviado correctamente la data'}
    return jsonify(res)
