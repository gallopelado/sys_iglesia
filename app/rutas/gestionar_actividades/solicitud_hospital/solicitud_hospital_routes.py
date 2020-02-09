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


@soh.route('/form_visita/<int:id>', methods=['GET'])
def editarFormulario(id):        
    form = FormularioVisita()                    
    lista = soli.obtenerSolicitudId(id)    
    if lista:
        idsolicitud = lista[0]
        form.solicitante.data = lista[1]
        form.descripcion.data = lista[2]
        form.paciente.data = lista[3]
        form.esmiembro.data = lista[5]
        form.estaenterado.data = lista[6]
        form.idioma.data = lista[7]
        form.hospital.data = lista[8]
        form.nrocuarto.data = lista[9]
        form.telefcuarto.data = lista[10]
        form.fechaadmision.data = lista[11]
        form.diagnostico.data = lista[12]
        form.direccionhospi.data = lista[13]
        form.horariovisita.data = lista[14]       
        form.lunes.data = lista[15]
        form.martes.data = lista[16]               
        form.miercoles.data = lista[17]
        form.jueves.data = lista[18]
        form.viernes.data = lista[19]
        form.sabado.data = lista[20]
        form.domingo.data = lista[21]    
    return render_template('solicitud_hospital/form_visita.html', titulo='Editar visita a hospital', form=form, idsolicitud=idsolicitud, bloqueado=False)


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
            soli.insertSolicitudHospital(solicitanteid, vhdes.upper(), pacienteid, vhesmiembro, vhestaenterado, 
            idioma, vhnombrehospi.upper(), vhnrocuarto, vhnrotelcuarto, vhfechaadmi, vhdiagnostico.upper(), 
            vhdirehospi.upper(), vhhoravisi, vhlunes, vhmartes, vhmiercoles, vhjueves, vhviernes, 
            vhsabado, vhdomingo, None, vhestado)
        else:
            ##MODIFICAR
            soli.updateSolicitudHospital(solicitanteid, pacienteid, idioma, vhdes.upper(), vhesmiembro, 
            vhestaenterado, vhnombrehospi.upper(), vhnrocuarto, vhnrotelcuarto, 
            vhfechaadmi, vhdiagnostico.upper(), vhdirehospi.upper(), vhhoravisi, vhlunes, 
            vhmartes, vhmiercoles, vhjueves, vhviernes, vhsabado, 
            vhdomingo, None, idsolicitud)

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
@soh.route('/get_solicitudes_json/<string:estado>')
def getSolicitudes(estado):    
    if estado in ('ATENDIDO', 'NO-ATENDIDO', 'CANCELADO'):
        res = soli.obtenerSolicitudes(estado)
        return jsonify(res)
    return jsonify({'estado':False, 'mensaje':'El parametro no es correcto'})

