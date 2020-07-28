from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.rutas.gestionar_cursos.asistencia_alumnos.AsistenciaAlumnoServices import AsistenciaAlumnoServices
asial = Blueprint('asistencia_alumnos', __name__, template_folder='templates')

@asial.route('/')
def index():
    return render_template('asistencia_alumnos/index.html', titulo="Registrar asistencia de alumnos")

# AJAX
@asial.route('/lista_profesor_cursos_asignatura/<int:idmalla>/<string:turno>/<int:idprofesor>')
def getListaProfesorCursosAsignatura(idmalla, turno, idprofesor):
    asi = AsistenciaAlumnoServices()
    data = asi.getListaProfesorCursosAsignatura(idmalla, turno, idprofesor)
    return jsonify(data)