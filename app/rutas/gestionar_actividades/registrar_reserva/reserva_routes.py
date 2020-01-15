#from datetime import date
# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos
from app.Models.actividad_models.ActividadAnualModel import ActividadAnualModel
from app.Models.actividad_models.ReservaModel import ReservaModel
from app.Models.ReferencialModel import ReferencialModel
from app.helps.helps import fechaActual
# Clase del formulario
from app.rutas.gestionar_actividades.registrar_reserva.formularios import FormAgregar
# Registrar módulo
# res -- registrar reserva
res = Blueprint('registrar_reserva', __name__, template_folder='templates')
titulo = 'Registrar reserva para eventos'
refm = ReferencialModel()
# Instancias
actim = ActividadAnualModel()
resm = ReservaModel()
@res.route('/')
def index_reserva():    
    return render_template('registrar_reserva/index.html', titulo=titulo)


@res.route('/form_reserva', methods=['GET'])
def mostrarFormulario():
    form = FormAgregar()               
    form.anho.data = resm.obtenerAnhoActivo()            
    return render_template('registrar_reserva/form_reserva.html', titulo='Formulario Reserva', form=form)


@res.route('/registrar', methods=['POST'])
def registrar():
    anho_habilitado = int(resm.obtenerAnhoActivo())        
    form = FormAgregar()
    res = form.validate_on_submit()
     # Set datos    
    idreserva = request.form['idreserva']
    anhohabil = int(form.anho.data)
    solicitante = form.solicitante.data
    evento = form.evento.data    
    lugar = form.lugar.data
    fechainicio = form.fechainicio.data
    horainicio = form.horainicio.data
    fechafin = form.fechafin.data
    horafin = form.horafin.data    
    obs = form.obs.data
    if res:
        next = request.args.get('next', None)
        if next:
            return redirect(next) 
       
        # Validar mas!
        if  fechainicio > fechafin:
            flash('La fecha de inicio no puede ser mayor a la fecha de finalizacion', 'warning')
            return redirect(url_for('actividades_anuales.mostrarFormulario'))
        elif anho_habilitado > anhohabil:
            flash('El año hábil no es correcto!', 'warning')
            return redirect(url_for('actividades_anuales.mostrarFormulario'))

        if idreserva is None or idreserva == '':
            ##REGISTRAR
            res = resm.guardarReserva('registrar', None, anhohabil, evento, lugar, solicitante, 
            fechainicio, horainicio, fechafin, horafin, obs, None, None)
        else:
            ##MODIFICAR
            res = resm.guardarReserva('modificar', idreserva, anhohabil, evento, lugar, solicitante, 
            fechainicio, horainicio, fechafin, horafin, obs, None, None)

        if res == True:
            flash('Se ha registrado una reserva', 'success')
            return redirect(url_for('registrar_reserva.index_reserva'))
        else:
            flash(res.diag.message_primary , 'danger')
            return redirect(url_for('registrar_reserva.index_reserva'))
    else:
        flash('Error en al cargar en formulario', 'danger')
        return redirect(url_for('registrar_reserva.mostrarFormulario'))    


@res.route('/form_actividad/modificar/<int:anho>/<int:id>', methods=['GET'])
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
        return render_template('registrar_reserva/form_reserva.html', titulo='Formulario Actividad', form=form, idactividad=id)

    return render_template('registrar_reserva/error_anho.html', titulo='El año no es válido')


@res.route('/eliminar/<int:anho>/<int:id>', methods=['GET'])
def eliminarActividad(anho,id):
    res = actim.guardarActividad('eliminar', id, anho, None, None, None, None, None, None,
	                            None, None, None, None, None)
    if res == True:
        flash('Se ha eliminado una actividad', 'success')
        return redirect(url_for('actividades_anuales.index_acti_anuales'))
    flash(res.diag.message_primary, 'warning')        
    return redirect(url_for('actividades_anuales.index_acti_anuales'))

## Funciones para AJAX
@res.route('/get_reservas_json', methods=['POST'])
def get_actividades_json():
    estado = request.json['estado'] 
    res = resm.obtenerReservasJson(estado)       
    return jsonify(res)


@res.route('/verificarAnho/<int:anho>')
def verificarAnho(anho):
    res = actim.verificarAnho(anho) if True else False
    return jsonify(res)


@res.route('/verificarAnhoFuturo/<int:anho>')
def verificarAnhoFuturo(anho):
    res = actim.verificarAnhoFuturo(anho)
    return jsonify(res)