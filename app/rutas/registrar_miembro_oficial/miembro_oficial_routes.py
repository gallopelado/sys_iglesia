# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelo

# Importar Modelo de Admision
from app.Models.FormAdmisionModel import FormAdmisionModel

# Importar Modelo MiembroOficialModel.
from app.Models.MiembroOficialModel import MiembroOficialModel

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
    
    # Procesar variables
    idmiembro = request.json['idmiembro']
    razonaltaid = request.json['idrazonalta']
    fechaconversion = request.json['fechaconversion']
    fechabautismo = request.json['fechabautismo']
    estadomembresia = request.json['estadomembresia']
    lugarbautismo = request.json['lugarbautismo']
    oficiador = request.json['ministro']
    fechainiciomembresia = request.json['fechainiciomembresia']
    bautizadoeniglesia = request.json['fuebautizado']
    padresmiembros = request.json['padreseniglesia']
    recibioes = request.json['recibioes']
    obs = request.json['observacion']


    # Enviar al Modelo.
    m = MiembroOficialModel()
    res = m.guardar(idmiembro, razonaltaid, fechaconversion, fechabautismo,
              lugarbautismo, oficiador, fechainiciomembresia, estadomembresia,
              bautizadoeniglesia, padresmiembros, recibioes, obs,
              0)
    if res:
        return jsonify({"guardado":True})
    
    return jsonify({"guardado": False})
