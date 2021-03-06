# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelo
from app.Models.RequisitoRefModel import RequisitoRefModel

reqi = Blueprint('requisito', __name__, template_folder='templates')

@reqi.route('/')
def index_requisito():
    return 'Referencial requisito'


# Rutas para AJAX
@reqi.route('/lista_requisito')
def listaRequisito():

    req = RequisitoRefModel()
    lista = req.getAllRequisitosJson()
    
    return jsonify(lista[0])