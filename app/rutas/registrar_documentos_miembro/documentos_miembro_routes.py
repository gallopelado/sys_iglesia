# Se importan las librerias basicas
from flask import current_app as app, current_app as app, Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar referenciales varios y helpers
from app.rutas.registrar_documentos_miembro.referenciales import *
from app.helps.helps import guardarDocumento, verificaNull

# Importar modelo
from app.Models.FormDocumentosModel import FormDocumentosModel

# Registrar la ruta en Blueprint
docm = Blueprint('registrar_documentos_miembro',
                 __name__, template_folder='templates')

# Definir rutas
@docm.route('/')
def index_documentos():
    return render_template('registrar_documentos_miembro/index.html')


@docm.route('/frm_docu')
def frmDocu():

    return render_template('registrar_documentos_miembro/formulario_registrar.html')

# Rutas para AJAX ##########
@docm.route('/lista_tipodocumentos')
def listaTipoDocumentos():

    return jsonify(obtenerTipoDocumentos())


@docm.route('/lista_personas_json')
def listaPersonas():

    return jsonify(obtenerPersonas())


@docm.route('/guardar_formulario', methods=['POST'])
def guardarFormulario():

    #print(f'Recibido: {str(request.form).encode("utf-8")}')
    #print(f'Documento: {request.files}')
    idtipodocumento = request.form['idtipodocumento']
    txt_fecha = request.form['txt_fecha']    
    idmiembro = request.form['idmiembro']
    idconyuge = verificaNull(request.form['idconyuge'] )
    oficiador = request.form['oficiador']
    declaracion = verificaNull(request.form['declaracion'] )
    notas = verificaNull(request.form['notas'] )
    testigo1 = verificaNull(request.form['testigo1'] )
    testigo2 = verificaNull(request.form['testigo2'] )
    documento_nombre = None
    
    if request.files:
        documento = request.files['documento_binario']
        documento_nombre = documento.filename
        

    doc = FormDocumentosModel()
    res = doc.guardar(idtipodocumento, txt_fecha, idmiembro, idconyuge, oficiador,
                documento_nombre, declaracion, notas, testigo1, testigo2)
    
    if res:        
        
        guardarDocumento(request, 'documento_binario', app, 'FORM_DOCUMENTOS_ARCHIVOS')
        return jsonify({"guardado": True})

    return jsonify({"guardado": False})
