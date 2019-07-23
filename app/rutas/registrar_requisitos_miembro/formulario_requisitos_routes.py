# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# importar modelo Requisitos.
from app.Models.RequisitoModel import RequisitoModel

# importar modelo Persona
from app.Models.PersonaModel import PersonaModel

# Registrar rutas en Blueprint
miereq = Blueprint('registrar_requisitos_miembro', __name__, template_folder='templates')

# Rutas
@miereq.route('/')
def index_miembrorequisitos():
    req = RequisitoModel()
    lista = req.listarPersonasActivas()    
    return render_template('registrar_requisitos_miembro/index.html', lista = lista)


@miereq.route('/frm_requisito')
def frmRequisito():
    return render_template('registrar_requisitos_miembro/frm_requisito.html')


# Rutas para AJAX
@miereq.route('/lista_requisitos')
def listaRequisitos():
    req = RequisitoModel()
    lista = req.listarTodo()[0]
    return jsonify(lista)

@miereq.route('/lista_personas_json')
def listaPersonas():
    per = PersonaModel()
    lista = per.listarPersonasJSON()
    return jsonify(lista[0][0])