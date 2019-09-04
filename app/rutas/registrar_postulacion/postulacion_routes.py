# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelos

postu = Blueprint('registrar_postulacion', __name__, template_folder='templates')

@postu.route('/')
def index_postulacion():

    return render_template('registrar_postulacion/index.html')


@postu.route('/frm_postulacion')
def frmPostulacion():

    return render_template('registrar_postulacion/formulario_postulacion.html')