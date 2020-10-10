from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from app.rutas.gestionar_cursos.asistencia_alumnos.AsistenciaAlumnoServices import AsistenciaAlumnoServices
asial = Blueprint('asistencia_alumnos', __name__, template_folder='templates')

@asial.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@asial.route('/')
def index():
    return render_template('asistencia_alumnos/index.html', titulo="Registrar asistencia de alumnos")

@asial.route('/form_asistencia')
def formAsistencia():
    return render_template('asistencia_alumnos/form_asistencia.html', titulo="Formulario asistencia")

# AJAX
@asial.route('/lista_profesor_cursos_asignatura/<int:idmalla>/<string:turno>/<int:idprofesor>/<int:idcurso>/<int:idasignatura>/<int:idnumeroasignatura>')
def getListaProfesorCursosAsignatura(idmalla, turno, idprofesor, idcurso, idasignatura, idnumeroasignatura):
    asi = AsistenciaAlumnoServices()
    data = asi.getListaProfesorCursosAsignatura(idmalla, turno, idprofesor, idcurso, idasignatura, idnumeroasignatura)
    return jsonify(data)

@asial.route('/lista_cursos_maestro/<int:idmalla>/<int:idprofesor>')
def getCursosMaestro(idmalla, idprofesor):
    asi = AsistenciaAlumnoServices()
    data = asi.getCursosMaestro(idmalla, idprofesor)
    return jsonify(data)

@asial.route('/lista_asignatura_maestro/<int:idmalla>/<int:idprofesor>/<int:idcurso>')
def getAsignaturaMaestro(idmalla, idprofesor, idcurso):
    asi = AsistenciaAlumnoServices()
    data = asi.getAsignaturaMaestro(idmalla, idprofesor, idcurso)
    return jsonify(data)

@asial.route('/lista_alumnos_curso/<int:idmalla>/<int:cur_id>/<int:asi_id>/<int:num_id>/<string:turno>')
def getListaAlumnosCurso(idmalla, cur_id, asi_id, num_id, turno):
    asi = AsistenciaAlumnoServices()
    data = asi.getListaAlumnosAsignatura(idmalla, cur_id, asi_id, num_id, turno)
    return jsonify(data)

@asial.route('/guardar_asistencia', methods=['POST'])
def guardarAsistencia():
    asi = AsistenciaAlumnoServices()
    res = asi.registrarAsistencias(request)
    return jsonify(res)

@asial.route('/get_formulario_asistencia/<int:malla_id>/<int:asi_id>/<int:num_id>/<int:per_id>/<string:turno>/<int:cur_id>/<string:fechaclase>', methods=['GET'])
def getFormularioAsistencia(malla_id, asi_id, num_id, per_id, turno, cur_id, fechaclase):
    asi = AsistenciaAlumnoServices()
    data = asi.getFormularioAsistencia(malla_id, asi_id, num_id, per_id, turno, cur_id, fechaclase)
    return jsonify(data)