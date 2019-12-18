# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelo
from app.Models.ReferencialModel import ReferencialModel

refs = Blueprint('referencial_simple', __name__, template_folder='templates')
refm = ReferencialModel()

@refs.route('/')
def index_requisito():
    return 'Referencial simple'


# Rutas para AJAX
@refs.route('/nuevo_registro', methods=['POST'])
def listaRequisito():
    #print(request.json)
    esquema = request.json['esquema'] 
    tabla = request.json['tabla']
    valor = request.json['valor']
    valor = valor.strip()
    valor = valor.strip('\n')
    valor = valor.upper()
    res = True if refm.nuevoRegistro(esquema, tabla, valor)==True else False
    return jsonify({"procesado":res})
    