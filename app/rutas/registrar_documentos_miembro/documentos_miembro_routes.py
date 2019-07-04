# Se importan las librerias basicas
from flask import current_app as app, Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Registrar la ruta en Blueprint
docm = Blueprint('registrar_documentos_miembro', __name__, template_folder='templates')

# Definir rutas
@docm.route('/')
def index_documentos():
    return render_template('registrar_documentos_miembro/index.html')

@docm.route('/frm_docu')
def frmDocu():
    return render_template('registrar_documentos_miembro/formulario_registrar.html')