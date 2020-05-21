# Librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json

from app.rutas.gestionar_cursos.planificacion_cursos.PlanificacionCursoServices import PlanificacionCursoServices
pcr = Blueprint('planificacion_cursos', __name__, template_folder='templates')

@pcr.route('/')
def index():
    return render_template('planificacion_cursos/index.html', titulo='Registrar Planificación de Cursos')

@pcr.route('/form_planificacion/<int:idmalla>')
def formPlanificacion(idmalla):
    return render_template('/planificacion_cursos/form_planificacion.html', titulo='Formulario planificación', idmalla=idmalla)

# AJAX
@pcr.route('/get_maestros')
def getMaestros():
    plans = PlanificacionCursoServices()
    return jsonify(plans.getMaestros())