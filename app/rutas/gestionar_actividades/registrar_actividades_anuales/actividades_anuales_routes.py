#from datetime import date
# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos
from app.Models.actividad_models.ActividadAnualModel import ActividadAnualModel
from app.Models.ReferencialModel import ReferencialModel
from app.helps.helps import fechaActual
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


@acan.route('/form_actividad/<int:anho>', methods=['GET'])
def mostrarFormulario(anho):
    if anho >= actim.verificarAnhoActivo(anho) and actim.verificarAnho(anho):
        form = FormAgregar()               
        form.anho.data = anho         
        #form.fechafin.data = date(1991, 12, 5)
        #x = date(1991, 12, 31).strftime('%Y/%m/%d')
        #print(x)

        return render_template('registrar_actividades_anuales/form_actividad.html', titulo='Formulario Actividad', form=form)

    return render_template('registrar_actividades_anuales/error_anho.html', titulo='El año no es válido')


@acan.route('/registrar', methods=['POST'])
def registrar():    
    form = FormAgregar()
    res = form.validate_on_submit()
    if res:
        next = request.args.get('next', None)
        if next:
            return redirect(next) 
        # Set datos
        opcion = 'registrar'
        anho = form.anho.data
        evento = form.evento.data
        comite = form.comite.data
        lugar = form.lugar.data
        fechainicio = form.fechainicio.data
        horainicio = form.horainicio.data
        fechafin = form.fechainicio.data
        horafin = form.horainicio.data
        plazo = form.plazo.data
        repite = form.repite.data
        obs = form.obs.data
        # Validar mas
        if not fechainicio > fechafin:
            flash('La fecha de inicio no puede ser mayor a la fecha de finalizacion')
            return redirect(url_for('actividades_anuales.mostrarFormulario', anho=anho))
        return "holi"
    else:
        return "Error en el formulario"    

## Funciones para AJAX
@acan.route('/get_actividades_json/<int:anho>')
def get_actividades_json(anho): 
    res = actim.obtenerActividadesJson(anho)       
    return jsonify(res)


@acan.route('/verificarAnho/<int:anho>')
def verificarAnho(anho):
    res = actim.verificarAnho(anho) if True else False
    return jsonify(res)


@acan.route('/verificarAnhoFuturo/<int:anho>')
def verificarAnhoFuturo(anho):
    res = actim.verificarAnhoFuturo(anho)
    return jsonify(res)