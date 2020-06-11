from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.rutas.gestionar_cursos.inscripcion_alumnos.InscripcionAlumnoServices import InscripcionAlumnoServices
insa = Blueprint('inscripcion_alumnos', __name__, template_folder='templates')

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