# Se importan las librerias basicas
from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos
from app.Models.actividad_models.ContratoReservaModel import ContratoReservaModel
from app.Models.actividad_models.ReservaModel import ReservaModel
# Registrar modulo
# gcr - generar contrato reserva
gcr = Blueprint('contrato_reserva', __name__, template_folder='templates')
titulo = 'Generar contrato por reserva'
crm = ContratoReservaModel()
rsm = ReservaModel()

@gcr.route('/')
def index_contrato():
    return render_template('contrato_reserva/index.html', titulo=titulo)


@gcr.route('/formulario_contrato')
def formularioContrato():
    titulo = 'Formulario contrato'
    hoy = date.today()    
    reservas = crm.obtenerReservasNoConfirmadas(hoy.year)
    encargados = crm.obtenerEncargados()    
    return render_template('contrato_reserva/formulario.html', titulo=titulo, reservas=reservas, encargados=encargados)


# Rutas para AJAX
@gcr.route('/obtener_reserva_id/<int:id>')
def obtenerReservaId(id):
    reserva = crm.obtenerDataReservaId(id)    
    return jsonify(reserva)