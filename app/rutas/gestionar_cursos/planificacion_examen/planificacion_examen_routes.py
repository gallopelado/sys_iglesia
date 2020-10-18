from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json, session
from app.Models.gestionar_cursos.planificacion_examen.PlanificacionExamen_dao import PlanificacionExamen_dao
from app.rutas.gestionar_cursos.planificacion_examen.Formulario import Formulario

ple = Blueprint('planificacion_examen', __name__, template_folder='templates')

@ple.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@ple.route('/')
def index():
    jusa_dao = PlanificacionExamen_dao()
    data = jusa_dao.getLista()
    return render_template('planificacion_examen/index.html', titulo='Registrar Planificación de exámenes', items = data)

@ple.route('/lista_alumnos/<int:malla_id>/<int:cur_id>/<int:asi_id>/<int:num_id>/<turno>')
def listaAlumnos(malla_id, cur_id, asi_id, num_id, turno):
    jusa_dao = PlanificacionExamen_dao()
    data = jusa_dao.getListaAlumnos(malla_id, cur_id, asi_id, num_id, turno)
    if not data:
        flash('No posee lista de alumnos', 'warning')
        return redirect(url_for('planificacion_examen.index'))
    form = Formulario()
    form.malla_id.data = malla_id
    form.cur_id.data = cur_id
    form.asi_id.data = asi_id
    form.num_id.data = num_id
    form.turno.data = turno
    return render_template('planificacion_examen/lista_alumnos.html', titulo='Lista de Alumnos con ausencias', items=data, form=form)

@ple.route('/formulario_planifica_examen/<int:malla_id>/<int:cur_id>/<int:asi_id>/<int:num_id>/<turno>/<int:per_id>')
def formularioPlanificaExamen(malla_id, cur_id, asi_id, num_id, turno, per_id):
    form = Formulario()
    form.malla_id.data = malla_id
    form.cur_id.data = cur_id
    form.asi_id.data = asi_id
    form.num_id.data = num_id
    form.turno.data = turno
    form.idmaestro.data = per_id
    jusa_dao = PlanificacionExamen_dao()
    data = jusa_dao.getLista()
    examenes = jusa_dao.getListaExamenes(asi_id, num_id)
    examenes.insert(0, { 'exa_id':'', 'exa_nombre':'...' })
    form.examenes.choices = [ (str(item['exa_id']), item['exa_nombre']) for item in examenes ]
    lista_examenes_planificados = jusa_dao.getListaExamenesPlanificados(malla_id, cur_id, asi_id, num_id, turno, per_id)

    # Cargar datos de la cabecera
    for item in data:
        if item['malla_id'] == malla_id and item['cur_id'] == cur_id and item['asi_id'] == asi_id and item['num_id'] == num_id and item['turno'] == turno and item['per_id'] == per_id:
            form.maestro.data = item['docente']
            form.curso.data = item['cur_des']
            form.asignatura.data = f"{item['asi_des']} {item['num_des']}"
            form.turno.data = item['turno']

    return render_template('planificacion_examen/formulario_planifica_examen.html', titulo='Formulario Planificar Examen', form=form, items=lista_examenes_planificados)

@ple.route('/guardar', methods=['POST'])
def guardar():
    form = Formulario()
    if form.validate_on_submit():
        jusa_dao = PlanificacionExamen_dao()
        # malla_id, cur_id, asi_id, num_id, turno, per_id, exa_id, planex_fecha, planex_hora, creacion_usuario
        res = jusa_dao.guardar(form.malla_id.data, form.cur_id.data, form.asi_id.data, form.num_id.data, form.turno.data, form.idmaestro.data, form.examenes.data, form.fecha.data, form.hora.data, int(session['usu_id']))
        if res > 0:
            flash('Se guardó correctemente', 'success')
        else:
            flash('Hubo un problema al intentar guardar', 'warning')
        return redirect(url_for('planificacion_examen.listaAlumnos', malla_id=form.malla_id.data, cur_id=form.cur_id.data, asi_id=form.asi_id.data, num_id=form.num_id.data, turno=form.turno.data))

@ple.route('/lista_justificativos_alumnos/<int:alumno_id>')
def listaJustificativosAlumno(alumno_id):
    #{{ url_for('planificacion_examen.listaAlumnos', malla_id=form.malla_id.data, cur_id=form.cur_id.data, asi_id=form.asi_id.data, num_id=form.num_id.data, turno=form.turno.data) }}
    jusa_dao = PlanificacionExamen_dao()
    data = jusa_dao.getListaJustificativosByAlumno(alumno_id)
    if not data:
        flash('No existen justificativos para este alumno', 'warning')
        return redirect(url_for('planificacion_examen.index'))
    return render_template('planificacion_examen/lista_justificativos_alumnos.html', titulo='Lista de Justificativos por alumno', items=data)