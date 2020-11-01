from datetime import date, datetime
# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
# Importar modelos
from app.Models.actividad_models.SolicitudHospitalModel import SolicitudHospitalModel
# Clase del formulario
from app.rutas.gestionar_actividades.solicitud_hospital.formularios import FormularioVisita
# Registrar módulo
# soh -- solicitud hospital
soh = Blueprint('solicitud_hospital', __name__, template_folder='templates')
titulo = 'Registrar solicitud para visita a Hospital'
# Instancias
soli = SolicitudHospitalModel()

@soh.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

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


@soh.route('/ver_formulario/<int:id>', methods=['GET'])
def verFormulario(id):        
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
    return render_template('solicitud_hospital/form_visita.html', titulo='Ver visita a hospital', form=form, idsolicitud=idsolicitud, bloqueado=True)


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
    vhestado = 'NO-ATENDIDO'
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



@soh.route('/cancelar/<int:id>', methods=['GET'])
def cancelaSolicitud(id):
    res = soli.cancelaSolicitudHospital(id)
    if res == True:
        flash('Se ha cancelado una solicitud', 'danger')
        return redirect(url_for('solicitud_hospital.index'))
    flash('Existe un error al cancelar. Solicite ayuda al administrador', 'warning')        
    return redirect(url_for('solicitud_hospital.index'))

## Funciones para AJAX
@soh.route('/get_solicitudes_json/<string:estado>')
def getSolicitudes(estado):    
    if estado in ('ATENDIDO', 'NO-ATENDIDO', 'CANCELADO'):
        res = soli.obtenerSolicitudes(estado)
        return jsonify(res)
    return jsonify({'estado':False, 'mensaje':'El parametro no es correcto'})

@soh.route('/get_solicitudes_json_id/<int:id>')
def getSolicitudesIdJSON(id):    
    res = soli.obtenerSolicitudIdJSON(id)
    return jsonify(res)

@soh.route('/get_integrantes_comite/<int:id>')
def getIntegrantesComiteJSON(id):    
    res = soli.obtenerIntegrantesComite(id)
    return jsonify(res)
    

## Rutas para formulario de voluntarios
@soh.route('/voluntarios')
def indexVoluntario():
    return render_template('solicitud_hospital/index_voluntarios.html', titulo='Voluntarios')

@soh.route('/form_voluntarios')
def formVoluntarios():
    solicitudes = soli.obtenerSolicitudesVoluntario()    
    comites = soli.obtenerComitesActivos()    
    return render_template('solicitud_hospital/form_voluntarios.html', 
    titulo='Formulario encargar voluntarios', bloqueado=False, solicitudes=solicitudes, comites=comites, solicitud=None, voluntarios=None, editar=False)

@soh.route('/modificar_voluntarios/<int:lvo_id>', methods=["GET"])
def modificarFormVoluntarioVoluntario(lvo_id):    
    solicitudes = soli.obtenerSolicitudesVoluntario()
    solicitud = soli.obtenerListaVoluntarioId(lvo_id)    
    comites = soli.obtenerComitesActivos() 
    voluntarios = soli.obtenerIntegrantesComite(solicitud['idcomite']) 
    voluntariosRegistrados = soli.obtenerVoluntariosRegistrados(lvo_id)
    return render_template('solicitud_hospital/form_voluntarios.html', 
    titulo='Formulario encargar voluntarios', bloqueado=False, solicitudes=solicitudes, comites=comites, 
    solicitud=solicitud, voluntarios=voluntarios, editar=True, voluntariosRegistrados=voluntariosRegistrados, lvo_id=lvo_id)

@soh.route('/ver_voluntarios/<int:id>', methods=["GET"])
def verFormVoluntarioVoluntario(id):    
    solicitudes = soli.obtenerSolicitudesVoluntario()
    solicitud = soli.obtenerListaVoluntarioId(id)    
    comites = soli.obtenerComitesActivos() 
    voluntarios = soli.obtenerIntegrantesComite(solicitud['idcomite']) 
    voluntariosRegistrados = soli.obtenerVoluntariosRegistrados(id)
    return render_template('solicitud_hospital/form_voluntarios.html', 
    titulo='Formulario encargar voluntarios', bloqueado=True, solicitudes=solicitudes, comites=comites, 
    solicitud=solicitud, voluntarios=voluntarios, editar=True, voluntariosRegistrados=voluntariosRegistrados)

## Ajax para voluntarios
@soh.route('/registar_lista', methods=['POST'])
def registraVoluntarios():
    idcomite = request.json['idcomite']    
    fechavisita = request.json['fechavisita']
    horavisita = request.json['horavisita']
    idsolicitud = request.json['idsolicitud']
    obs = request.json['obs']
    voluntarios = request.json['voluntarios'] 
    
    try:
        res = soli.registrarListaSolicitudVoluntarios(idsolicitud, fechavisita, horavisita, idcomite, 
        obs.upper(), None, voluntarios)
        if res:
            flash('Se ha procesado con exito', 'success')
            return jsonify({'estado':res, 'mensaje':'Insercion exitosa'})
        flash('Error al procesar. Favor contacte con el Administrado', 'danger')            
        return jsonify({'estado':False, 'mensaje':'Error al intentar insertar lista de voluntarios'})
    except Exception:
        print('Error al intentar insertar lista de voluntarios')
        flash('Error al procesar. Favor contacte con el Administrado', 'danger')            
        return jsonify({'estado':False, 'mensaje':'Error al intentar insertar lista de voluntarios'})

@soh.route('/obtener_lista_voluntarios', methods=['GET'])
def listaVoluntarios():
    lista = soli.obtenerListasVoluntario()
    return jsonify(lista)

@soh.route('/obtener_lista_voluntarios/<int:id>', methods=['GET'])
def obtenerDatosFormularioVoluntario(id):
    solicitud = soli.obtenerListaVoluntarioId(id)  
    print(solicitud)  
    return jsonify(solicitud)

@soh.route('/eliminar_voluntario/<int:idlista>/<int:idvoluntario>', methods=['GET'])
def eliminarVoluntario(idlista, idvoluntario):
    res = soli.eliminarVoluntario(idlista, idvoluntario)
    if res==True:
        flash('Voluntario eliminado con exito', 'success')  
        return jsonify({'estado':res, 'mensaje':'Voluntario eliminado con exito'})
    flash('Problemas al eliminar voluntario', 'danger')
    return jsonify({'estado':False, 'mensaje':'Problemas al eliminar voluntario'})

@soh.route('/agregar_voluntario/<int:idlista>/<int:idvoluntario>', methods=['GET'])
def agregarVoluntario(idlista, idvoluntario):
    res = soli.agregarVoluntario(idlista, idvoluntario)
    if res==True:
        flash('Voluntario agregado con exito', 'success')  
        return jsonify({'estado':res, 'mensaje':'Voluntario agregado con exito'})
    flash('Problemas al agregar voluntario', 'danger')
    return jsonify({'estado':False, 'mensaje':'Problemas al agregar voluntario'})

@soh.route('/actualizar_lista_voluntario', methods=['PUT'])
def actualizarListaVoluntario():
    lvo_id = request.json['lvo_id']
    idsolicitud = request.json['idsolicitud']
    fechavisita = request.json['fechavisita']
    horavisita = request.json['horavisita']
    obs = request.json['obs']
    res = soli.actualizarListaVoluntario(lvo_id, idsolicitud, fechavisita, horavisita, obs.upper(), session['usu_id'])
    if res==True:
        flash('Se ha procesado con exito', 'success')  
        return jsonify({'estado':res, 'mensaje':'Se ha procesado con exito'})
    flash('Problemas al procesar', 'danger')
    return jsonify({'estado':False, 'mensaje':'Problemas al procesar'})

@soh.route('/baja_lista_voluntario', methods=['PUT'])
def bajaListaVoluntario():
    idsolicitud = request.json['idsolicitud']
    res = soli.eliminarListaVoluntario(idsolicitud)
    if res==True:
        flash('Se ha procesado con exito', 'success')  
        return jsonify({'estado':res, 'mensaje':'Se ha procesado con exito'})
    flash('Problemas al procesar', 'danger')
    return jsonify({'estado':False, 'mensaje':'Problemas al procesar'})

## Rutas para formulario registro de informes
@soh.route('/informevisitas')
def indexInformeVisitas():
    return render_template('solicitud_hospital/index_informes.html', titulo='Informes de visitas')

@soh.route('/form_informe')
def formInformes():
    solicitudes = soli.obtenerSolicitudesEstado()    
    print(solicitudes)    
    return render_template('solicitud_hospital/form_informe.html', 
    titulo='Formulario informe-visita', bloqueado=False, solicitudes=solicitudes, idsolicitud=None, voluntarios=None, editar=None)

@soh.route('/editar_informe/<int:id>')
def editarInforme(id):
    solicitudes = soli.obtenerSolicitudesEstado()      
    return render_template('solicitud_hospital/form_informe.html', 
    titulo='Formulario informe-visita', bloqueado=False, solicitudes=solicitudes, idsolicitud=id, voluntarios=None, editar=True)

@soh.route('/ver_informe/<int:id>')
def verInforme(id):
    solicitudes = soli.obtenerSolicitudesEstado()      
    return render_template('solicitud_hospital/form_informe.html', 
    titulo='Formulario informe-visita', bloqueado=True, solicitudes=solicitudes, idsolicitud=id, voluntarios=None, editar=True)

## AJAX para informes
@soh.route('/get_informes')
def getInformes():
    informes = soli.obtenerInformes()
    return jsonify(informes)

@soh.route('/get_informes/<int:id>')
def getInformesId(id):
    informes = soli.obtenerInformeId(id)
    return jsonify(informes)  

@soh.route('/get_voluntarios_por_lista/<int:id>')
def getVoluntariosPorLista(id):
    solicitudes = soli.obtenerVoluntariosPorLista(id)
    return jsonify(solicitudes) 

@soh.route('/nuevo_informe', methods=['POST'])
def nuevoInforme():
    descripcion = request.json['descripcion']
    idlista = request.json['idsolicitud']
    idvoluntario = request.json['voluntarios']
    nuevo = soli.insertInformeVisita(idlista, idvoluntario, descripcion, None)
    if nuevo==True:
        flash('Se ha procesado con exito', 'success')
        return jsonify({'estado':True, 'mensaje':'Se ha procesado con exito'})
    flash('Error al procesar', 'danger')
    return jsonify({'estado':False, 'mensaje':'Error al procesar'})

@soh.route('/modificar_informe', methods=['PUT'])
def modificarInforme():
    descripcion = request.json['descripcion']
    idlista = request.json['idsolicitud']
    idvoluntario = request.json['voluntarios']
    modificar = soli.updateInformeVisita(idlista, idvoluntario, descripcion, None)
    if modificar==True:
        flash('Se ha procesado con exito', 'success')
        return jsonify({'estado':True, 'mensaje':'Se ha procesado con exito'})
    flash('Error al procesar', 'danger')
    return jsonify({'estado':False, 'mensaje':'Error al procesar'})