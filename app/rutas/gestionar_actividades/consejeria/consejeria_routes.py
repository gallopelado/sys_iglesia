from datetime import date, datetime
# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,session
# Importar modelos
from app.Models.actividad_models.ConsejeriaModel import ConsejeriaModel
# Clase del formulario
from app.rutas.gestionar_actividades.consejeria.formularios import Formulario
# Registrar módulo
# cmi -- consejeria miembro
cmi = Blueprint('consejeria', __name__, template_folder='templates')
titulo = 'Registrar solicitud de consejeria para miembros'
# Instancias
cm = ConsejeriaModel()

@cmi.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@cmi.route('/')
def index():
    return render_template('consejeria/index.html', titulo=titulo)

@cmi.route('/formulario_solicitud')
def formulario():
    form = Formulario()    
    return render_template('consejeria/form_solicitud.html', titulo=titulo, form=form, editar=False, bloqueado=False)

@cmi.route('/editar_solicitud/<int:id>')
def editarFormulario(id):
    form = Formulario()
    return render_template('consejeria/form_solicitud.html', titulo=titulo, form=form, idsolicitud=id, editar=True, bloqueado=False)

@cmi.route('/ver_solicitud/<int:id>')
def verFormulario(id):
    form = Formulario()
    return render_template('consejeria/form_solicitud.html', titulo=titulo, form=form, idsolicitud=id, editar=False, bloqueado=True)

@cmi.route('/registrar', methods=['POST'])
def registrar():
    print(request.form)
    form = Formulario()
    res = form.validate_on_submit()
    idsolicitud = request.form['idsolicitud']
    idmiembro = int(form.miembro.data)
    idreligion =  int(form.religion.data)
    asisteregular = form.asiste_regular.data
    serviciocentral = form.servicio_central.data
    grupo_creci = form.grupo_creci.data
    serviciosemanal = form.servicio_semanal.data
    descri_matriant = form.descri_matriant.data.upper()
    descri_hijos = form.descri_hijos.data.upper()
    grupo_asiste = int(form.grupo_asiste.data)
    consultagrupo = form.grupo_creci.data
    descri_recibio = form.descri_recibio.data.upper()
    descri_asesoria = form.descri_asesoria.data.upper()
    consejero = int(form.consejero.data)

    if res:
        next = request.args.get('next', None)
        if next:
            return redirect(next)

        if idsolicitud is None or idsolicitud == '':
            ##REGISTRAR
            cm.insertSolicitud(idmiembro, idreligion, consejero, grupo_asiste, serviciocentral, grupo_creci, serviciosemanal, 
            descri_matriant, descri_hijos, consultagrupo, descri_recibio, descri_asesoria,'ATENDIDO', None, None)
        else:
            ##MODIFICAR
            cm.updateSolicitud(idsolicitud, idmiembro, idreligion, consejero, grupo_asiste, serviciocentral, grupo_creci, serviciosemanal, 
            descri_matriant, descri_hijos, consultagrupo, descri_recibio, descri_asesoria, None, None, None)
        
        if res == True:
            flash('Se ha realizado la operacion con exito', 'success')
            return redirect(url_for('consejeria.index'))
        else:
            flash('Problemas al validar formulario' , 'danger')
            return redirect(url_for('consejeria.index'))

    else:
        flash('Error en al cargar en formulario', 'danger')
        return redirect(url_for('consejeria.index'))

@cmi.route('/cancela_solicitud/<int:id>')
def cancelaSolicitud(id):    
    res = cm.cancelaSolicitud(id)
    if res == True:
        flash('Se cancelo dicha solicitud', 'warning')
        return redirect(url_for('consejeria.index'))
    flash('Error al cancelar dicha solicitud', 'danger')
    return redirect(url_for('consejeria.index'))

## Ajax
@cmi.route('/get_miembros/<int:id>')
def getMiembros(id):    
    miembros = cm.getMiembroId(id)
    return jsonify(miembros)

@cmi.route('/get_solicitudes')
def getSolicitudes():    
    solicitudes = cm.getSolicitudes()
    return jsonify(solicitudes)

@cmi.route('/get_solicitud_id/<int:id>')
def getSolicitudId(id):    
    solicitud = cm.getSolicitudId(id)
    return jsonify(solicitud)