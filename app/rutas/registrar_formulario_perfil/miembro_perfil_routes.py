# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelos
from app.Models.MiembroPerfilModel import MiembroPerfilModel

perfil = Blueprint('registrar_formulario_perfil', __name__, template_folder='templates')

@perfil.route('/')
def index_perfil():
    p = MiembroPerfilModel()
    lista = p.listar()
    return render_template('registrar_formulario_perfil/index.html', lista=lista)


@perfil.route('/form_perfil')
def formPerfil():
    return render_template('registrar_formulario_perfil/formulario_perfil.html')


@perfil.route('/form_perfil', methods=['POST'])
def procesarPerfil():
    
    print(request.form)

    return "probando POST"

