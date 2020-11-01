# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,session

# importar modelo Requisitos.
from app.Models.RequisitoModel import RequisitoModel

# importar modelo Persona
from app.Models.PersonaModel import PersonaModel

# Registrar rutas en Blueprint
miereq = Blueprint('registrar_requisitos_miembro', __name__, template_folder='templates')

# Rutas
@miereq.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@miereq.route('/')
def index_miembrorequisitos():
    req = RequisitoModel()
    lista = req.listarPersonasActivas()    
    return render_template('registrar_requisitos_miembro/index.html', lista = lista)


@miereq.route('/frm_requisito/<int:idpersona>', methods=['GET'])
def ver(idpersona):
    id = int(idpersona)

    req = RequisitoModel()
    lista = req.getDataPersonaRequisito(id)
    listacab = req.getNombre(id)
    
    return render_template('registrar_requisitos_miembro/frm_requisito.html', lista_requi = lista, lista_cab = listacab)

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

@miereq.route('/guardar', methods=['POST'])
def guardar():

    #print(f'Recibido {request.json}')
    idpersona = request.json['idpersona']
    idrequisitos = request.json['idrequisitos']
    observaciones = request.json['observaciones']
    
    req = RequisitoModel()
    res = req.guardar(idpersona, idrequisitos, observaciones)
    if res:
        return jsonify({"guardado": True})
    
    return jsonify({"guardado": False})

@miereq.route('/eliminar', methods=['POST'])
def eliminar():
    print(f'Recibido {request.json}')
    idpersona = request.json['idpersona']
    idrequisito = request.json['idrequisito']

    req = RequisitoModel()
    res = req.eliminar(idpersona, idrequisito)
    if res:
        return jsonify({"eliminado": True})
    
    return jsonify({"eliminado": False})
