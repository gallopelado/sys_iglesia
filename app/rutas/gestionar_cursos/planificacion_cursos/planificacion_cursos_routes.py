# Librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json

pcr = Blueprint('planificacion_cursos', __name__, template_folder='templates')

@pcr.route('/')
def index():
    return render_template('planificacion_cursos/index.html', titulo='Registrar Planificación de Cursos')

@pcr.route('/form_planificacion')
def formPlanificacion():
    return render_template('/planificacion_cursos/form_planificacion.html', titulo='Formulario planificación')