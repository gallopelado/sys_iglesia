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
    plantillas = crm.obtenerPlantilla(None)        
    return render_template('contrato_reserva/formulario.html', titulo=titulo, reservas=reservas, encargados=encargados, plantillas=plantillas)


# Rutas para AJAX
@gcr.route('/obtener_reserva_id/<int:id>')
def obtenerReservaId(id):
    reserva = crm.obtenerDataReservaId(id)    
    return jsonify(reserva)


@gcr.route('/obtener_plantilla_id/<int:id>')
def obtenerPlantillaId(id):
    plantilla = crm.obtenerPlantilla(id)    
    return jsonify(plantilla)


@gcr.route('/obtener_encargado_id/<int:id>')
def obtenerEncargadoId(id):
    encargado = crm.obtenerEncargadoId(id)    
    return jsonify(encargado)


@gcr.route('/generar', methods=['POST'])
def generar():
    resid = request.json['idreserva'] 
    encargadoid = request.json['idencargado'] 
    plantillacontrato = request.json['plantilla'] 
    plantillatexto =  request.json['plantilla_texto']
    creadoporusuario = None
    if resid == '' and encargadoid == '' and plantillacontrato == '' and plantillatexto == '':
        flash('Error al procesar', 'warning')
        return jsonify({'estado': False, 'mensaje': 'Parametros vacios'})    
    res = crm.procesarContrato(resid, encargadoid, plantillacontrato, plantillatexto, creadoporusuario)
    if res==True:
        flash('Se generó con exito', 'success')
        return jsonify({'estado': res, 'mensaje': 'Se generó con exito'})
    flash('Error al procesar', 'warning')
    return jsonify({'estado': res, 'mensaje': 'Error al procesar'})
