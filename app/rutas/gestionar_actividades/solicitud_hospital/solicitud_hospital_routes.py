from datetime import date, datetime
# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos
from app.Models.actividad_models.ReservaModel import ReservaModel
from app.Models.actividad_models.SolicitudHospitalModel import SolicitudHospitalModel
# Clase del formulario
from app.rutas.gestionar_actividades.solicitud_hospital.formularios import FormularioVisita
# Registrar módulo
# soh -- solicitud hospital
soh = Blueprint('solicitud_hospital', __name__, template_folder='templates')
titulo = 'Registrar solicitud para visital a Hospital'
# Instancias
resm = ReservaModel()
soli = SolicitudHospitalModel()
@soh.route('/')
def index():    
    return render_template('solicitud_hospital/index.html', titulo=titulo)


@soh.route('/form_visita', methods=['GET'])
def formularioVisita():
    form = FormularioVisita()                           
    return render_template('solicitud_hospital/form_visita.html', titulo='Formulario visita a hospital', form=form, bloqueado=False)


@soh.route('/form_reserva/<int:id>', methods=['GET'])
def editarFormulario(id):
    hoy = date.today()
    hoy = datetime(hoy.year, hoy.month, hoy.day)
    bloqueado = False
    form = FormAgregar()               
    form.anho.data = resm.obtenerAnhoActivo()     
    lista = resm.obtenerReservaId(id)
    if lista:
        idreserva = lista[0]
        form.anho.data = lista[1]
        form.solicitante.data = lista[2]
        form.evento.data = lista[3]
        form.lugar.data = lista[4]
        form.fechainicio.data = lista[5]
        v_fechainicio = datetime(lista[5].year, lista[5].month, lista[5].day)
        form.horainicio.data = lista[6]
        form.fechafin.data = lista[7]
        form.horafin.data = lista[8]
        form.obs.data = lista[9] 
        if v_fechainicio < hoy:
            bloqueado = True            
        return render_template('solicitud_hospital/form_reserva.html', titulo='Formulario Reserva', form=form, idreserva=idreserva, bloqueado=bloqueado)
    flash('No existe esta reserva!', 'warning')
    return redirect(url_for('registrar_reserva.index_reserva'))


@soh.route('/registrar', methods=['POST'])
def registrar():         
    form = FormularioVisita()
    res = form.validate_on_submit()
     # Set datos    
    idsolicitud = request.form['idsolicitud']
    solicitanteid = form.solicitante.data
    vhdes = form.descripcion.data
    pacienteid = form.paciente.data    
    vhesmiembro = form.esmiembro.data
    vhestaenterado = form.estaenterado.data  
    idioma = form.idioma.data  
    vhnombrehospi = form.hospital.data
    vhnrocuarto = form.nrocuarto.data
    vhnrotelcuarto = form.telefcuarto.data
    fechaadmision = form.fechaadmision.data
    vhfechaadmi = datetime(fechaadmision.year, fechaadmision.month, fechaadmision.day)    
    vhdiagnostico = form.diagnostico.data    
    vhdirehospi = form.direccionhospi.data
    vhhoravisi = form.horariovisita.data
    vhlunes = form.lunes.data
    vhmartes = form.martes.data
    vhmiercoles = form.miercoles.data
    vhjueves = form.jueves.data
    vhviernes = form.viernes.data
    vhsabado = form.sabado.data
    vhdomingo = form.domingo.data
    vhestado = True
    if res:
        next = request.args.get('next', None)
        if next:
            return redirect(next)                

        if idsolicitud is None or idsolicitud == '':
            ##REGISTRAR
            soli.insertSolicitudHospital(solicitanteid, vhdes, pacienteid, vhesmiembro, vhestaenterado, 
            idioma, vhnombrehospi, vhnrocuarto, vhnrotelcuarto, vhfechaadmi, vhdiagnostico, 
            vhdirehospi, vhhoravisi, vhlunes, vhmartes, vhmiercoles, vhjueves, vhviernes, 
            vhsabado, vhdomingo, None, vhestado)
        else:
            ##MODIFICAR
            pass

        if res == True:
            flash('Se ha realizado la operacion con exito', 'success')
            return redirect(url_for('solicitud_hospital.index'))
        else:
            flash(res.diag.message_primary , 'danger')
            return redirect(url_for('solicitud_hospital.index'))
    else:
        flash('Error en al cargar en formulario', 'danger')
        return redirect(url_for('solicitud_hospital.index'))    



@soh.route('/eliminar/<int:id>', methods=['GET'])
def eliminarReserva(id):
    res = resm.guardarReserva('cancelar', id, None, None, None, None, 
            None, None, None, None, None, None, None)
    if res == True:
        flash('Se ha cancelado una reserva', 'default')
        return redirect(url_for('registrar_reserva.index_reserva'))
    flash(res.diag.message_primary, 'warning')        
    return redirect(url_for('registrar_reserva.index_reserva'))

## Funciones para AJAX
@soh.route('/get_reservas_json', methods=['POST'])
def get_actividades_json():
    estado = request.json['estado'] 
    res = resm.obtenerReservasJson(estado)       
    return jsonify(res)

