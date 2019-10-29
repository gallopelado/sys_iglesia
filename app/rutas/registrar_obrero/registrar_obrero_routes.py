# Se importan las librerías básicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelo
from app.Models.ComiteModel import ComiteModel

# Importar formularios
from app.rutas.registrar_obrero.formularios import *

# Registrar en Blueprint
ob = Blueprint('registrar_obrero', __name__, template_folder='templates')
titulo = 'Registrar Obreros a Comité'
tituloFormObrero = 'Formulario Lista de Obreros'
cm = ComiteModel()

# Rutas
@ob.route('/')
def index_obrero():    
    lista = cm.traerTodos()       
    return render_template('registrar_obrero/index.html', titulo=titulo, lista=lista)


@ob.route('/formulario_obrero/<int:idcomite>', methods=['GET'])
def formularioObrero(idcomite):    
    comite = cm.traerPorId(idcomite)
    form = FormAgregar() 
    # Setear formulario
    form.idcomite.data = comite[0]
    form.comite.data = comite[1] 
    form.idlider.data = comite[2]
    form.lider.data = comite[3]  
    return render_template('registrar_obrero/formulario.html', titulo=tituloFormObrero, comite=comite, form=form)