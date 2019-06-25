# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar el modelo principal.
from app.Models.FormAdicionalModel import FormAdicionalModel

# Combos necesarios para ciertas vistas.
from app.rutas.registrar_formulario_adicional.combos import *

# Registrar la ruta en Blueprint
formadi = Blueprint('registrar_formulario_adicional', __name__, template_folder='templates')

# Rutas

@formadi.route('/')
def index_formadi():

    adi = FormAdicionalModel()

    datos = adi.listarFormularios()

    return render_template('registrar_formulario_adicional/index.html', datos = datos)

@formadi.route('/frm_adi')
def frm_adi():

    # Combos.
    lista_nac = listaNacionalidades()
    lista_san = listaSangre()
    lista_prof = listaProfesion()

    return render_template('registrar_formulario_adicional/frm_adicional.html', lista_nac = lista_nac, lista_san = lista_san, lista_prof = lista_prof)


    """Funcion listaProfesion.
    
    Crea instancia del modelo y retorna lista.

    """
    prof = ProfesionModel()

    return prof.listarTodos()  