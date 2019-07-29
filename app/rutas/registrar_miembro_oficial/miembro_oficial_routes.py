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
