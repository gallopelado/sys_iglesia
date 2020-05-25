# Librerias basicas
import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json

from app.rutas.gestionar_cursos.planificacion_cursos.PlanificacionCursoServices import PlanificacionCursoServices
pcr = Blueprint('planificacion_cursos', __name__, template_folder='templates')

@pcr.route('/')
def index():
    return render_template('planificacion_cursos/index.html', titulo='Registrar Planificación de Cursos')

@pcr.route('/form_planificacion/<int:idmalla>')
def formPlanificacion(idmalla):
    return render_template('/planificacion_cursos/form_planificacion.html', titulo='Formulario planificación', idmalla=idmalla)

@pcr.route('/form_frecuencia_asignatura')
def formFrecuenciaAsignatura():
    return render_template('/planificacion_cursos/form_frecuencia_asignatura.html', titulo='Formulario frecuencia de asignatura')

# AJAX
@pcr.route('/get_maestros')
def getMaestros():
    plans = PlanificacionCursoServices()
    return jsonify(plans.getMaestros())

@pcr.route('/get_detalle_asignaturas/<int:idplan>/<int:idcurso>')
def getDetalleAsignaturas(idplan, idcurso):
    plans = PlanificacionCursoServices()
    return jsonify(plans.getDetalleAsignaturas(idplan, idcurso)) 

@pcr.route('/agregar_curso', methods=['POST'])
def agregarCurso():
    malla_id = request.json['malla_id']
    cur_id = request.json['cur_id']
    plans = PlanificacionCursoServices()
    res = plans.registrarCurso(malla_id, cur_id)
    return jsonify(res)

@pcr.route('/agregar_asignatura', methods=['POST'])
def agregarAsignatura():
    malla_id = request.json['malla_id']
    asi_id = request.json['asi_id']
    cur_id = request.json['cur_id']
    num_id = request.json['num_id']
    per_id = request.json['per_id']
    fechainicio = request.json['fecha_inicio']
    fechafin = request.json['fecha_fin']
    turno = request.json['turno']
    plans = PlanificacionCursoServices()
    res = plans.registrarDetallePlan(malla_id, asi_id, num_id, per_id, cur_id, fechainicio, fechafin, turno)
    return jsonify(res)


@pcr.route('/get_fecha_actual')
def getFechaActual():
    fecha = datetime.datetime.now().strftime('%Y-%m-%d')
    return jsonify({'fecha_actual':fecha})

@pcr.route('/get_detalle_frecuencia/<int:malla_id>/<int:asi_id>/<int:num_id>/<int:per_id>/<int:cur_id>/<string:turno>')
def getDetalleFrecuencia(malla_id, asi_id, num_id, per_id, cur_id, turno):
    plans = PlanificacionCursoServices()
    lista = plans.getDetalleFrecuencia(malla_id, asi_id, num_id, per_id, cur_id, turno)
    return jsonify(lista)

@pcr.route('/agregar_horario_asignatura', methods=['POST'])
def agregarHorarioAsignatura():
    malla_id = request.json['malla_id']
    asi_id = request.json['asi_id']
    cur_id = request.json['cur_id']
    num_id = request.json['num_id']
    per_id = request.json['per_id']
    horainicio = request.json['hora_inicio']
    horafin = request.json['hora_fin']
    dia = request.json['dia']
    turno = request.json['turno']
    plans = PlanificacionCursoServices()
    res = plans.registrarDetalleFrecuencia(malla_id, asi_id, num_id, turno, per_id, dia, cur_id, horainicio, horafin)
    return jsonify(res)

@pcr.route('/eliminar_horario_asignatura', methods=['POST'])
def eliminarHorarioAsignatura():
    id = request.json['id']
    plans = PlanificacionCursoServices()
    res = plans.eliminarAsignaturaFrecuencia(id)
    return jsonify(res)