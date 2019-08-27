# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelos
from app.Models.MiembroPerfilModel import MiembroPerfilModel

perfil = Blueprint('registrar_miembro_perfil', __name__, template_folder='templates')

@perfil.route('/')
def index_perfil():

    p = MiembroPerfilModel()
    lista = p.listar()
    print(lista)
    return 'Index miembro perfil'

