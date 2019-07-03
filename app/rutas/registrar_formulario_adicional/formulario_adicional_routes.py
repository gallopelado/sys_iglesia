# Se importa la biblioteca del sistema operativo 
import os
# Se importan las librerias basicas
from flask import current_app as app, Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar el modelo principal.
from app.Models.FormAdicionalModel import FormAdicionalModel

# Combos necesarios para ciertas vistas.
from app.rutas.registrar_formulario_adicional.combos import *

# Registrar la ruta en Blueprint
formadi = Blueprint('registrar_formulario_adicional', __name__, template_folder='templates')

# Rutas

@formadi.route('/')
def index_formadi():

    adi = FormAdicionalModel()

    datos = adi.listarFormularios()

    return render_template('registrar_formulario_adicional/index.html', datos = datos)

@formadi.route('/frm_adi/<idadi>')
def frm_adi(idadi):
    
    # Se obtiene el nombre de la foto, se envía a la vista.
    adm = FormAdicionalModel()
    lista_datos_admision = adm.obtenerDatosId(idadi)

    # Combos.
    lista_nac = listaNacionalidades()
    lista_san = listaSangre()
    lista_prof = listaProfesion()
    
    return render_template('registrar_formulario_adicional/frm_adicional.html', lista_nac = lista_nac, 
            lista_san = lista_san, lista_prof = lista_prof, lista_datos_admision = lista_datos_admision)

#################
# Rutas para AJAX
@formadi.route('/obtener_frmdatos_id', methods=['POST'])
def obtenerDatosId():

    idadi = request.json['idadi']   

    adi = FormAdicionalModel()        
     
    return jsonify(adi.obtenerDatosId(idadi))

@formadi.route('/obtener_frmdatos_id_json', methods=['POST'])
def obtenerDatosIdJSON():

    idadi = request.json['idadi']

    adi = FormAdicionalModel()

    return jsonify(adi.obtenerDatosIdJSON(idadi))

@formadi.route('/obtener_historial_profesiones', methods=['POST'])
def obtenerHistorialProfesionesId():

    idadi = request.json['idadi']   

    adi = FormAdicionalModel()        

    return jsonify(adi.obtenerHistorialProfesionesId(idadi))

@formadi.route('/eliminar_historial', methods=['POST'])
def eliminarHistorial():

    #print(str(request.json).encode('utf-8'))
    idpersona = request.json["id"]
    idprofesion = request.json["idprofesion"]
    puesto_laboral = request.json["puesto"]
    lugar_trabajo = request.json["lugar"]

    adi = FormAdicionalModel()
    res = adi.eliminarHistorial(idpersona, idprofesion, puesto_laboral, lugar_trabajo)

    if res == True:
        return jsonify({"eliminado": True})
    
    return jsonify({"eliminado": False})
    

@formadi.route('/image_upload', methods=['POST'])
def image_upload():

    #print(f"Recibido : {request.files['foto']}")

    if request.files:

        idadi = request.form['idadi']
        imagen = request.files['foto']
        
        # Se procede a guardar en el directorio.
        imagen.save(os.path.join(app.config['FORM_ADICIONAL_IMAGENES'], imagen.filename))           

        # Obtener lista de fotos guardadas.
        listaFotos = os.listdir(app.config['FORM_ADICIONAL_IMAGENES'])

        # Recorrer las fotos.
        for i in listaFotos:
            
            # Separar nombre de foto en lista de ['8', 'jpg'] utilizando el punto.
            nombreFoto = i.split('.')     
            
            # Verificar el idadi con el el primer índice de la lista.
            if nombreFoto[0] == idadi:

                # Volver a concantenar el nombre de la foto.
                encontrado = f"{nombreFoto[0]}.{nombreFoto[1]}"
                
                # Concatenar a la ruta y guardar en la base de datos.
                # paso 1: Guardar nombre en bd.
                adim = FormAdicionalModel()
                adim.guardarNombreFoto(idadi, encontrado)
                return jsonify({'guardado': True})

    return jsonify({'guardado': True})

@formadi.route('/guardar_formulario', methods=['POST'])
def guardar_formulario():

    #print(f"Recibido : {request.json}")

    datos_formulario = request.json['datos_formulario']
    datos_tabla_nuevos = request.json['datos_tabla_nuevos']
    datos_tabla_eliminar = request.json['datos_tabla_eliminar']

    idpersona = datos_formulario['idpersona'] if datos_formulario['idpersona'] != '' else None
    idnacionalidad = datos_formulario['idnacionalidad'] if datos_formulario['idnacionalidad'] != '' else None
    lugarnacimiento = datos_formulario['lugarnacimiento'] if datos_formulario['lugarnacimiento'] != '' else None
    alergias = datos_formulario['alergias'] if datos_formulario['alergias'] != '' else None
    tiposangre = datos_formulario['tiposangre'] if datos_formulario['tiposangre'] != '' else None
    capacidad_diferente = datos_formulario['capacidad_diferente'] if datos_formulario['capacidad_diferente']!= '' else None

    adi = FormAdicionalModel()
    res = adi.guardarFormulario(idpersona, idnacionalidad, lugarnacimiento, alergias, tiposangre, capacidad_diferente, 
    datos_tabla_nuevos, datos_tabla_eliminar)
    
    if res == True:
        return jsonify({'guardado': True})
