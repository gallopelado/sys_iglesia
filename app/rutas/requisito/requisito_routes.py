# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,session,abort

# Importar modelo
from app.Models.RequisitoRefModel import RequisitoRefModel

reqi = Blueprint('requisito', __name__, template_folder='templates')

@reqi.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo'] not in ('ADMIN'):
        abort(403, description="Acceso prohibido")

@reqi.route('/')
def index_requisito():
    return 'Referencial requisito'


# Rutas para AJAX
@reqi.route('/lista_requisito')
def listaRequisito():

    req = RequisitoRefModel()
    lista = req.getAllRequisitosJson()
    
    return jsonify(lista[0])