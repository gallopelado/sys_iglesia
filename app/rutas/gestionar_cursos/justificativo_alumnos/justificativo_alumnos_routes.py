from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json, session
from app.Models.gestionar_cursos.justificativo_alumno.JustificativoAlumno_dao import JustificativoAlumno_dao
from app.rutas.gestionar_cursos.justificativo_alumnos.Formulario import Formulario

jusa = Blueprint('justificativo_alumno', __name__, template_folder='templates')

@jusa.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@jusa.route('/')
def index():
    jusa_dao = JustificativoAlumno_dao()
    data = jusa_dao.getLista()
    return render_template('justificativo_alumnos/index.html', titulo='Registrar Justificativos de Ausencia', items = data)

@jusa.route('/lista_alumnos/<int:malla_id>/<int:cur_id>/<int:asi_id>/<int:num_id>/<turno>')
def listaAlumnos(malla_id, cur_id, asi_id, num_id, turno):
    jusa_dao = JustificativoAlumno_dao()
    data = jusa_dao.getListaAlumnos(malla_id, cur_id, asi_id, num_id, turno)
    if not data:
        flash('No posee lista de alumnos', 'warning')
        return redirect(url_for('justificativo_alumno.index'))
    form = Formulario()
    form.malla_id.data = malla_id
    form.cur_id.data = cur_id
    form.asi_id.data = asi_id
    form.num_id.data = num_id
    form.turno.data = turno
    return render_template('justificativo_alumnos/lista_alumnos.html', titulo='Lista de Alumnos con ausencias', items=data, form=form)

@jusa.route('/formulario_ausencia/<int:malla_id>/<int:cur_id>/<int:asi_id>/<int:num_id>/<turno>/<int:per_id>/<fecha_clase>')
def formularioAusencia(malla_id, cur_id, asi_id, num_id, turno, per_id, fecha_clase):
    form = Formulario()
    form.malla_id.data = malla_id
    form.cur_id.data = cur_id
    form.asi_id.data = asi_id
    form.num_id.data = num_id
    form.turno.data = turno
    form.alu_id.data = per_id
    form.fecha_clase.data = fecha_clase
    jusa_dao = JustificativoAlumno_dao()
    data = jusa_dao.getListaAlumnos(malla_id, cur_id, asi_id, num_id, turno)

    for item in data:
        if item['per_id'] == per_id:
            form.alumno.data = item['estudiante']
            form.curso.data = item['cur_des']
            form.asignatura.data = item['asignatura']
            form.idmaestro.data = item['idmaestro']

    return render_template('justificativo_alumnos/formulario_ausencia.html', titulo='Formulario Ausencia', form=form)

@jusa.route('/guardar', methods=['POST'])
def guardar():
    form = Formulario()
    if form.validate_on_submit():
        jusa_dao = JustificativoAlumno_dao()
        res = jusa_dao.guardar(form.alu_id.data, form.malla_id.data, form.cur_id.data, form.asi_id.data, form.num_id.data, form.idmaestro.data, form.turno.data, form.descripcion.data.upper(), form.fecha_clase.data, int(session['usu_id']))
        if res > 0:
            flash('Se guardó correctemente', 'success')
        else:
            flash('Hubo un problema al intentar guardar', 'warning')
        return redirect(url_for('justificativo_alumno.listaAlumnos', malla_id=form.malla_id.data, cur_id=form.cur_id.data, asi_id=form.asi_id.data, num_id=form.num_id.data, turno=form.turno.data))

@jusa.route('/lista_justificativos_alumnos/<int:alumno_id>')
def listaJustificativosAlumno(alumno_id):
    #{{ url_for('justificativo_alumno.listaAlumnos', malla_id=form.malla_id.data, cur_id=form.cur_id.data, asi_id=form.asi_id.data, num_id=form.num_id.data, turno=form.turno.data) }}
    jusa_dao = JustificativoAlumno_dao()
    data = jusa_dao.getListaJustificativosByAlumno(alumno_id)
    if not data:
        flash('No existen justificativos para este alumno', 'warning')
        return redirect(url_for('justificativo_alumno.index'))
    return render_template('justificativo_alumnos/lista_justificativos_alumnos.html', titulo='Lista de Justificativos por alumno', items=data)