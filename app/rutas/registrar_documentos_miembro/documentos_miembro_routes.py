# Se importan las librerias basicas
from flask import current_app as app, Blueprint, render_template, request, redirect, url_for, flash, jsonify, session

# Importar referenciales varios y helpers
from app.rutas.registrar_documentos_miembro.referenciales import *
from app.helps.helps import guardarDocumento, verificaNull

# Importar modelo
from app.Models.FormDocumentosModel import FormDocumentosModel

# Registrar la ruta en Blueprint
docm = Blueprint('registrar_documentos_miembro',
                 __name__, template_folder='templates')

@docm.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

# Definir rutas
@docm.route('/')
def index_documentos():
    return render_template('registrar_documentos_miembro/index.html')

@docm.route('/frm_docu')
def frmDocu():

    return render_template('registrar_documentos_miembro/formulario_registrar.html')

@docm.route('/frm_mod')
def frmMod():
    
    return render_template('registrar_documentos_miembro/formulario_modificar.html')

# Rutas para AJAX ##########
@docm.route('/lista_miembros_documento')
def listaMiembrosDocumento():
    
    doc = FormDocumentosModel()
    lista = doc.listarMiembrosDocumentos()
    
    return jsonify(lista)

@docm.route('/obtener_miembro_documento', methods=['POST'])
def obtenerMiembroDocumento():
    
    #print(f'RECIBIDO = {request.json}')
    idmiembro = request.json['idmiembro']
    idtipodocumento = request.json['idtipodocumento']
    doc = FormDocumentosModel()
    lista = doc.obtenerMiembroDocumento(idmiembro, idtipodocumento)
    #print(str(lista[0][0]).encode('utf-8'))
    return jsonify(lista[0][0])

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
        flash("Exito, se registró correctamente", "success")
        return jsonify({"guardado": True})        

    return jsonify({"guardado": False})


@docm.route('/modificar_formulario', methods=['POST'])
def modificarFormulario():

    id_antiguo_tipodocumento = request.form['id_antiguo_tipodocumento']
    idtipodocumento = request.form['idtipodocumento']
    txt_fecha = request.form['txt_fecha']
    idmiembro = request.form['idmiembro']
    idconyuge = verificaNull(request.form['idconyuge'])
    oficiador = request.form['oficiador']
    declaracion = verificaNull(request.form['declaracion'])
    notas = verificaNull(request.form['notas'])
    testigo1 = verificaNull(request.form['testigo1'])
    testigo2 = verificaNull(request.form['testigo2'])
    documento_nombre = verificaNull(request.form['nombre_binario'])

    if request.files:
        documento = request.files['documento_binario']
        documento_nombre = documento.filename

    doc = FormDocumentosModel()
    res = doc.modificar(id_antiguo_tipodocumento, idtipodocumento, txt_fecha, idmiembro, idconyuge, oficiador,
                      documento_nombre, declaracion, notas, testigo1, testigo2)

    if res:
        
        guardarDocumento(request, 'documento_binario',
                         app, 'FORM_DOCUMENTOS_ARCHIVOS')
        flash("Exito, se modificó correctamente", "success")
        return jsonify({"guardado": True})

    return jsonify({"guardado": False})

@docm.route('/eliminar_formulario', methods=['POST'])
def eliminarFormulario():

    idpersona = request.json['idpersona']
    iddocumento = request.json['iddocumento']

    doc = FormDocumentosModel()
    res = doc.eliminar(idpersona, iddocumento)

    if res:        
        return jsonify({"estado": True})

    return jsonify({"estado": False})
