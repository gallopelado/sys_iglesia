from datetime import date, datetime
# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,session
# Importar modelos
from app.Models.actividad_models.ReservaModel import ReservaModel
# Clase del formulario
from app.rutas.gestionar_actividades.registrar_reserva.formularios import FormAgregar
# Registrar módulo
# res -- registrar reserva
res = Blueprint('registrar_reserva', __name__, template_folder='templates')
titulo = 'Registrar reserva para eventos'
# Instancias
resm = ReservaModel()

@res.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@res.route('/')
def index_reserva():    
    return render_template('registrar_reserva/index.html', titulo=titulo)


@res.route('/form_reserva', methods=['GET'])
def mostrarFormulario():
    form = FormAgregar()               
    form.anho.data = resm.obtenerAnhoActivo()            
    return render_template('registrar_reserva/form_reserva.html', titulo='Formulario Reserva', form=form, bloqueado=False)


@res.route('/form_reserva/<int:id>', methods=['GET'])
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
        return render_template('registrar_reserva/form_reserva.html', titulo='Formulario Reserva', form=form, idreserva=idreserva, bloqueado=bloqueado)
    flash('No existe esta reserva!', 'warning')
    return redirect(url_for('registrar_reserva.index_reserva'))


@res.route('/registrar', methods=['POST'])
def registrar():  
    hoy = date.today()
    hoy = datetime(hoy.year, hoy.month, hoy.day)    
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
    v_fechainicio = datetime(fechainicio.year, fechainicio.month, fechainicio.day)
    horainicio = form.horainicio.data
    fechafin = form.fechafin.data
    v_fechafin = datetime(fechafin.year, fechafin.month, fechafin.day)
    horafin = form.horafin.data    
    obs = form.obs.data
    if res:
        next = request.args.get('next', None)
        if next:
            return redirect(next) 
       
        # Validar mas!
        if  fechainicio > fechafin:
            flash('La fecha de inicio no puede ser mayor a la fecha de finalizacion', 'warning')
            return redirect(url_for('registrar_reserva.index_reserva'))                
        elif anho_habilitado > anhohabil:
            flash('El año hábil no es correcto!', 'warning')
            return redirect(url_for('registrar_reserva.index_reserva'))

        if idreserva is None or idreserva == '':
            ##REGISTRAR
            if v_fechainicio < hoy:
                flash('La fecha de inicio es menor a la actual', 'warning')
                return redirect(url_for('registrar_reserva.index_reserva'))
            elif v_fechafin < hoy:
                flash('La fecha de fin es menor a la actual', 'warning')
                return redirect(url_for('registrar_reserva.index_reserva')) 
            res = resm.guardarReserva('registrar', None, anhohabil, evento, lugar, solicitante, 
            fechainicio, horainicio, fechafin, horafin, obs, None, None)
        else:
            ##MODIFICAR
            res = resm.guardarReserva('modificar', idreserva, anhohabil, evento, lugar, solicitante, 
            fechainicio, horainicio, fechafin, horafin, obs, None, None)

        if res == True:
            flash('Se ha realizado la operacion con exito', 'success')
            return redirect(url_for('registrar_reserva.index_reserva'))
        else:
            flash(res.diag.message_primary , 'danger')
            return redirect(url_for('registrar_reserva.index_reserva'))
    else:
        flash('Error en al cargar en formulario', 'danger')
        return redirect(url_for('registrar_reserva.mostrarFormulario'))    



@res.route('/eliminar/<int:id>', methods=['GET'])
def eliminarReserva(id):
    res = resm.guardarReserva('cancelar', id, None, None, None, None, 
            None, None, None, None, None, None, None)
    if res == True:
        flash('Se ha cancelado una reserva', 'default')
        return redirect(url_for('registrar_reserva.index_reserva'))
    flash(res.diag.message_primary, 'warning')        
    return redirect(url_for('registrar_reserva.index_reserva'))

## Funciones para AJAX
@res.route('/get_reservas_json', methods=['POST'])
def get_actividades_json():
    estado = request.json['estado'] 
    res = resm.obtenerReservasJson(estado)       
    return jsonify(res)

