# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelos
from app.Models.MiembroPerfilModel import MiembroPerfilModel
from app.Models.ReferencialModel import ReferencialModel

perfil = Blueprint('registrar_formulario_perfil', __name__, template_folder='templates')

@perfil.route('/')
def index_perfil():
    p = MiembroPerfilModel()
    lista = p.listar()
    return render_template('registrar_formulario_perfil/index.html', lista=lista)


@perfil.route('/form_perfil/<int:idmiembro>', methods=['GET'])
def formPerfil(idmiembro):

    id = idmiembro

    # Obtener lista de ministerios.
    referencial = ReferencialModel()
    ministerios = referencial.getAll('referenciales.ministerios')

    # Obtener datos de miembro por id.
    miembro = MiembroPerfilModel()
    perfil = miembro.obtenerMiembroId(id)[0]

    # Procesar los ministerios 
    lista = perfil[2]
    minis = None
    if lista:
        print(lista.split(','))
        minis = lista.split(',')    

    return render_template('registrar_formulario_perfil/formulario_perfil.html', ministerios = ministerios, perfil = perfil, minis = minis)


@perfil.route('/form_perfil', methods=['POST'])
def procesarPerfil():
    
    print(request.form)

    return "probando POST"

