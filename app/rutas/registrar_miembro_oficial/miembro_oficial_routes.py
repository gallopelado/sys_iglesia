# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelo

# Importar Modelo de Admision
from app.Models.FormAdmisionModel import FormAdmisionModel

# Registrar las rutas en Blueprint
mieofi = Blueprint('registrar_miembro_oficial', __name__, template_folder='templates')


@mieofi.route('/')
def index_mieofi():
    return render_template('registrar_miembro_oficial/index.html')


@mieofi.route('/frm_miembro')
def frmMiembro():
    return render_template('registrar_miembro_oficial/formulario_miembro.html')


# Rutas para AJAX.
@mieofi.route('/personas_activas')
def personasActivas():

    adm = FormAdmisionModel()
    lista = adm.getAdmisionesActivas(True)
    
    return jsonify(lista[0][0])


@mieofi.route('/guardar', methods=['POST'])
def guardar():
    print(f'Recibido {request.json}')

    # Procesar variables
    idmiembro = request.json['idmiembro']
    idrazonalta = request.json['idrazonalta']
    fechaconversion = request.json['fechaconversion']
    fechabautismo = request.json['fechabautismo']
    estadomembresia = request.json['estadomembresia']
    lugarbautismo = request.json['lugarbautismo']
    ministro = request.json['ministro']
    fechainiciomembresia = request.json['fechainiciomembresia']
    fuebautizado = request.jsonn['fuebautizado']
    padreseniglesia = request.json['padreseniglesia']
    recibioes = request.json['recibioes']
    observacion = request.json['observacion']

    return jsonify({"guardando":True})
