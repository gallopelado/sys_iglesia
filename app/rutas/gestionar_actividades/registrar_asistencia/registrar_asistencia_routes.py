# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos
from app.Models.actividad_models.AsistenciaModel import AsistenciaModel
from app.Models.PersonaModel import PersonaModel
from app.Models.ReferencialModel import ReferencialModel
from app.helps.helps import fechaActual, fechaFormatoLargo

# Registrar modulo
asis = Blueprint('registrar_asistencia', __name__, template_folder='templates')
refm = ReferencialModel()
perm = PersonaModel()
asism = AsistenciaModel()
titulo = 'Registrar asistencias de miembros de la iglesia'

@asis.route('/')
def index_asistencia():
    lista = asism.obtenerAsistencias(True)    
    print(lista)
    return render_template('registrar_asistencia/index.html', titulo=titulo, lista=lista)


@asis.route('/formulario_asistencia')
def formularioAsistencia():
    evento = refm.getAll('referenciales.eventos')
    fecha = fechaFormatoLargo(fechaActual())
    persona = perm.listarPersonas()         
    return render_template('registrar_asistencia/formulario.html', titulo='Formulario Asistencia', evento=evento, fecha=fecha, persona=persona)


@asis.route('/formulario_asistencia/<int:id>')
def formularioAsistenciaMod(id):
    asistencia = asism.obtenerAsistenciasPorId(id)    
    evento = refm.getAll('referenciales.eventos')
    fecha = fechaFormatoLargo(fechaActual())    
    if asistencia:                
        idasistencia = asistencia[0][0]
        return render_template('registrar_asistencia/formulario.html', titulo='Formulario Asistencia', evento=evento, fecha=fecha, asistencia=asistencia, idasistencia=idasistencia)
    flash('No existe dicha lista', 'danger')
    return redirect(url_for('registrar_asistencia.index_asistencia'))


@asis.route('/formulario_ver/<int:id>')
def formularioVer(id):
    asistencia = asism.obtenerAsistenciasPorId(id)    
    evento = refm.getAll('referenciales.eventos')
    fecha = fechaFormatoLargo(fechaActual())    
    if asistencia:                
        idasistencia = asistencia[0][0]
        return render_template('registrar_asistencia/formulario.html', titulo='Formulario Asistencia', evento=evento, fecha=fecha, asistencia=asistencia, idasistencia=idasistencia, ver=True)
    flash('No existe dicha lista', 'danger')
    return redirect(url_for('registrar_asistencia.index_asistencia'))


@asis.route('/guardar', methods=['POST'])
def guardar():
    print(request.json)
    opcion = request.json['opcion']
    idasistencia = request.json['idasistencia']    
    cbo_evento = request.json['cbo_evento']
    txt_obs = request.json['txt_obs']
    cadena_persona = request.json['cadena_persona']
    cadena_asistio = request.json['cadena_asistio']
    cadena_puntual = request.json['cadena_puntual']
    if txt_obs == '' or cbo_evento == '':
        return jsonify({'estado':False, 'mensaje':'Se ha enviado vacio el evento o la descripcion'})

    if opcion == 'registrar':
        res = asism.procesar(opcion, None, cbo_evento, txt_obs, cadena_persona, cadena_asistio, cadena_puntual)
        flash('Exito al guardar', 'success') if res==True else flash('Hubo un error', 'danger')
        return jsonify({'estado':res, 'mensaje':'Exito al guardar'}) if res==True else jsonify({'estado':res, 'mensaje':'Hubo un error'})
    elif opcion == 'modificar':
        res = asism.procesar(opcion, idasistencia, cbo_evento, txt_obs, cadena_persona, cadena_asistio, cadena_puntual)
        flash('Exito al modificar', 'success') if res==True else flash('Hubo un error', 'danger')
        return jsonify({'estado':res, 'mensaje':'Exito al modificar'}) if res==True else jsonify({'estado':res, 'mensaje':'Hubo un error'})
    
    return jsonify({'estado':False, 'mensaje':'Los parametros no son correctos'})


@asis.route('/eliminar/<int:id>', methods=['GET'])
def eliminar(id):
    res = asism.procesar('baja', id, None, None, None, None, None)
    if res==True:
        flash('Se ha eliminado una lista', 'warning')
        return redirect(url_for('registrar_asistencia.index_asistencia'))
    else:
        flash('Hubo un problema al eliminar. Favor contacte con el administrador', 'danger')
        return redirect(url_for('registrar_asistencia.index_asistencia'))