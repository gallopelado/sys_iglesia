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
    return render_template('justificativo_alumnos/lista_alumnos.html', titulo='Lista de Alumnos con ausencias', items=data)

@jusa.route('/formulario_ausencia')
def formularioAusencia():
    form = Formulario()
    return render_template('justificativo_alumnos/formulario_ausencia.html', titulo='Formulario Ausencia', form=form)

@jusa.route('/lista_justificativos_alumnos')
def listaJustificativoAlumno():
    return render_template('justificativo_alumnos/lista_justificativos_alumnos.html', titulo='Lista de Justificativos por alumno')