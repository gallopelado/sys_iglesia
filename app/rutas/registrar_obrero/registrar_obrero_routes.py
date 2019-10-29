# Se importan las librerías básicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelo
from app.Models.ComiteModel import ComiteModel

# Registrar en Blueprint
ob = Blueprint('registrar_obrero', __name__, template_folder='templates')
titulo = 'Registrar Obreros a Comité'


# Rutas
@ob.route('/')
def index_obrero():
    cm = ComiteModel()
    lista = cm.traerTodos()
    return render_template('registrar_obrero/index.html', titulo=titulo, lista=lista)