# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Se importa el modelo.
from app.Models.ListaCalificadosModel import ListaCalificadosModel
from app.Models.ListaCandidatoModel import ListaCandidatoModel

# Registrar Blueprint
cali = Blueprint('registrar_calificados', __name__, template_folder='templates')

# Generar instancias del modelo.
calim = ListaCalificadosModel()
candim = ListaCandidatoModel()

titulo = 'Registrar Lista de Calificados'

@cali.route('/')
def index_calificados():
    res = calim.obtenerPostulaciones()    
    return render_template('registrar_calificados/index.html', titulo=titulo, lista=res)


@cali.route('/formulario/<int:idpostulacion>', methods=['GET'])
def revisar(idpostulacion):
    titulo = 'Formulario Evaluación'
    lista = candim.traerListaCandidatos(idpostulacion)
    isAdmitidos = True if calim.nroAdmitidos(idpostulacion) > 0 else False    
    detalle = lista[4] if len(lista[4])>0 else None      
    calificados = calim.verificaCalificados(idpostulacion)
    return render_template('registrar_calificados/formulario.html', titulo=titulo, lista=lista, detalle=detalle, isAdmitidos=isAdmitidos, calificados=calificados)


# Rutas para AJAX
@cali.route('/traer_perfil_id/<int:idperfil>', methods=['GET'])
def traerPerfilId(idperfil):
    res = calim.traerInfoPerfil(idperfil)    
    return jsonify(res)


@cali.route('/guardar_lista', methods=['POST'])
def guardarLista():
    print(request.json)

    idpostulacion = request.json['idpostulacion']
    candidatos = request.json['candidatos']

    if idpostulacion and candidatos:
        res = calim.guardarCalificados(idpostulacion, candidatos)
        if res:
            return jsonify({'estado':True, 'mensaje':'Se ha guardado correctamente'})
    else:
        return jsonify({'estado':False, 'error':'Hubo problemas al recibir los datos!'})
    