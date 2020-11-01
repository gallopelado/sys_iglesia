from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,session
from app.rutas.gestionar_cursos.inscripcion_alumnos.InscripcionAlumnoServices import InscripcionAlumnoServices
insa = Blueprint('inscripcion_alumnos', __name__, template_folder='templates')

@insa.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@insa.route('/')
def index():
    return render_template('inscripcion_alumnos/index.html', titulo='Inscripción de alumnos')

@insa.route('/form_inscripcion')
def formInscripcion():
    return render_template('inscripcion_alumnos/form_inscripcion.html', titulo='Formulario inscripción')

@insa.route('/form_asignatura')
def formAsignatura():
    return render_template('inscripcion_alumnos/form_asignatura.html', titulo='Formulario asignatura')

# AJAX
@insa.route('/get_cursos_planificados')
def getCursosPlanificados():
    ins = InscripcionAlumnoServices()
    data = ins.getCursosPlanificados()
    return jsonify(data)

@insa.route('/get_personas')
def getPersonas():
    ins = InscripcionAlumnoServices()
    data = ins.getPersonas()
    return jsonify(data)

@insa.route('/get_lista_alumnos_registrados/<int:malla_id>/<int:curso_id>')
def getListaAlumnosRegistrados(malla_id, curso_id):
    ins = InscripcionAlumnoServices()
    data = ins.getListaAlumnosRegistrados(malla_id, curso_id)
    return jsonify(data)

@insa.route('/inscribir_alumno', methods=['POST'])
def inscribirAlumno():
    alumno = {
        'malla_id': request.json['malla_id'], 'curso_id': request.json['curso_id'], 'per_id': request.json['per_id']
    }
    ins = InscripcionAlumnoServices()
    data = ins.inscribirAlumnoCurso(alumno)
    return jsonify(data)

@insa.route('/actualizar_estado_inscripcion_alumno', methods=['PUT'])
def actualizarEstadoInscripcionAlumno():
    alumno = {
        'malla_id': request.json['malla_id'], 'curso_id': request.json['curso_id'], 'per_id': request.json['per_id']
    }
    ins = InscripcionAlumnoServices()
    data = ins.actualizarEstadoInscripcionAlumno(alumno)
    return jsonify(data)

##Endpoints para el formulario asignatura
@insa.route('/get_asignaturas/<int:malla_id>/<int:curso_id>')
def getAsignaturas(malla_id, curso_id):
    ins = InscripcionAlumnoServices()
    data = ins.obtenerAsignaturas(malla_id, curso_id)
    return jsonify(data)

@insa.route('/get_asignaturas_alumno/<int:malla_id>/<int:curso_id>/<int:per_id>')
def getAsignaturasAlumno(malla_id, curso_id, per_id):
    ins = InscripcionAlumnoServices()
    data = ins.obtenerAsignaturasAlumno(malla_id, curso_id, per_id)
    return jsonify(data)

@insa.route('/guardar_asignatura_alumno', methods=['POST'])
def guardarAsignaturaAlumno():
    ins = InscripcionAlumnoServices()
    res = {}
    #asignatura['malla_id'], asignatura['curso_id'], asignatura['per_id'], asignatura['asi_id'], asignatura['num_id'], asignatura['turno']
    res['malla_id'] = request.json['malla_id']
    res['curso_id'] = request.json['curso_id']
    res['per_id'] = request.json['per_id']
    res['asi_id'] = request.json['asi_id']
    res['num_id'] = request.json['num_id']
    res['turno'] = request.json['turno']
    data = ins.guardarAsignaturaAlumno(res)
    return jsonify(data)

@insa.route('/anular_asignatura_alumno', methods=['PUT'])
def anularAsignaturaAlumno():
    ins = InscripcionAlumnoServices()
    res = {}
    res['malla_id'] = request.json['malla_id']
    res['curso_id'] = request.json['curso_id']
    res['per_id'] = request.json['per_id']
    res['asi_id'] = request.json['asi_id']
    res['num_id'] = request.json['num_id']
    res['turno'] = request.json['turno']
    data = ins.anularAsignaturaAlumno(res)
    return jsonify(data)