# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos
from app.Models.actividad_models.ActividadAnualModel import ActividadAnualModel
from app.Models.ReferencialModel import ReferencialModel
# Clase del formulario
from app.rutas.gestionar_actividades.registrar_actividades_anuales.formularios import FormAgregar
# Registrar módulo
# acan -- actividad anual
acan = Blueprint('actividades_anuales', __name__, template_folder='templates')
titulo = 'Registrar actividades anuales de la organización'
# Instancias
actim = ActividadAnualModel()
@acan.route('/')
def index_acti_anuales():
    lista = actim.obtenerAnho()
    return render_template('registrar_actividades_anuales/index.html', titulo=titulo, anhos=lista)


@acan.route('/form_actividad/<int:idanho>', methods=['GET'])
def mostrarFormulario(idanho):
    form = FormAgregar()
    refm = ReferencialModel()
    
    form.anho.data = idanho 
    form.evento.choices = refm.getAll('referenciales.eventos')
    form.comite.choices = refm.getAll('referenciales.ministerios')
    form.lugar.choices = refm.getAll('referenciales.lugares')
    form.plazo.choices = refm.getAll('referenciales.plazos')
    
    return render_template('registrar_actividades_anuales/form_actividad.html', titulo='Formulario Actividad', form=form)


## Funciones para AJAX
@acan.route('/get_actividades_json/<int:anho>')
def get_actividades_json(anho): 
    res = actim.obtenerActividadesJson(anho)       
    return jsonify(res)