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
     # Set datos
    opcion = 'registrar'
    idactividad = request.form['idactividad']
    anhohabil = form.anho.data
    evento = form.evento.data
    comite = form.comite.data
    lugar = form.lugar.data
    fechainicio = form.fechainicio.data
    horainicio = form.horainicio.data
    fechafin = form.fechafin.data
    horafin = form.horafin.data
    plazo = form.plazo.data
    repite = form.repite.data
    obs = form.obs.data
    if res:
        next = request.args.get('next', None)
        if next:
            return redirect(next) 
       
        # Validar mas
        if  fechainicio > fechafin:
            flash('La fecha de inicio no puede ser mayor a la fecha de finalizacion', 'warning')
            return redirect(url_for('actividades_anuales.mostrarFormulario', anho=anhohabil))
        
        if idactividad is None or idactividad == '':
            res = actim.guardarActividad(opcion, None, anhohabil, evento, lugar, fechainicio, horainicio, fechafin, horafin,
	                            plazo, repite, obs, comite, None)
        else:
            res = actim.guardarActividad('modificar', idactividad, anhohabil, evento, lugar, fechainicio, horainicio, fechafin, horafin,
	                            plazo, repite, obs, comite, None)

        if res == True:
            flash('Se ha registrado una actividad', 'success')
            return redirect(url_for('actividades_anuales.index_acti_anuales'))
        else:
            flash(res.diag.message_primary , 'danger')
            return redirect(url_for('actividades_anuales.index_acti_anuales', anho=anhohabil))
    else:
        flash('Error en al cargar en formulario', 'danger')
        return redirect(url_for('actividades_anuales.mostrarFormulario', anho=anhohabil))    


@acan.route('/form_actividad/modificar/<int:anho>/<int:id>', methods=['GET'])
def modificarFormulario(anho, id):
    if anho >= actim.verificarAnhoActivo(anho) and actim.verificarAnho(anho):
        res = actim.obtenerActividadesId(id)                   
        form = FormAgregar()                       
        form.anho.data = anho                 
        form.evento.data = res[2]
        form.comite.data = res[3]
        form.lugar.data = res[4]
        form.fechainicio.data = res[5]
        form.horainicio.data = res[6]
        form.fechafin.data = res[7]
        form.horafin.data = res[8]
        form.plazo.data = res[9]
        form.repite.data = res[10]
        form.obs.data = res[11]
        return render_template('registrar_actividades_anuales/form_actividad.html', titulo='Formulario Actividad', form=form, idactividad=id)

    return render_template('registrar_actividades_anuales/error_anho.html', titulo='El año no es válido')


@acan.route('/eliminar/<int:anho>/<int:id>', methods=['GET'])
def eliminarActividad(anho,id):
    res = actim.guardarActividad('eliminar', id, anho, None, None, None, None, None, None,
	                            None, None, None, None, None)
    if res == True:
        flash('Se ha eliminado una actividad', 'success')
        return redirect(url_for('actividades_anuales.index_acti_anuales'))
    flash(res.diag.message_primary, 'warning')        
    return redirect(url_for('actividades_anuales.index_acti_anuales'))

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