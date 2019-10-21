# Se importan las librerías básicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelo

# Registrar en Blueprint
comi = Blueprint('registrar_comite', __name__, template_folder='templates')

# Rutas
@comi.route('/')
def index_comite():
    return render_template('registrar_comite/index.html')

@comi.route('/formulario', methods=['GET'])
def formulario():
    return render_template('registrar_comite/formulario_comite.html')