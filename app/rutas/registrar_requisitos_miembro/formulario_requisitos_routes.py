# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Registrar rutas en Blueprint
miereq = Blueprint('registrar_requisitos_miembro', __name__, template_folder='templates')

# Rutas
@miereq.route('/')
def index_miembrorequisitos():
    return render_template('registrar_requisitos_miembro/index.html')

@miereq.route('/frm_requisito')
def frmRequisito():
    return render_template('registrar_requisitos_miembro/frm_requisito.html')
