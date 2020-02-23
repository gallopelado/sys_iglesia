from datetime import date, datetime
# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos
from app.Models.actividad_models.ConsejeriaModel import ConsejeriaModel
# Clase del formulario
from app.rutas.gestionar_actividades.consejeria.formularios import Formulario
# Registrar módulo
# cmi -- consejeria miembro
cmi = Blueprint('consejeria', __name__, template_folder='templates')
titulo = 'Registrar solicitud de consejeria para miembros'
# Instancias
cm = ConsejeriaModel()

@cmi.route('/')
def index():
    return render_template('consejeria/index.html', titulo=titulo)

@cmi.route('/formulario_solicitud')
def formulario():
    form = Formulario()
    miembros = cm.getMiembros()
    #print(miembros)
    return render_template('consejeria/form_solicitud.html', titulo=titulo, form=form)