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
        
        minis = lista.split(',')    

    return render_template('registrar_formulario_perfil/formulario_perfil.html', ministerios = ministerios, perfil = perfil, minis = minis)


@perfil.route('/form_perfil', methods=['POST'])
def procesarPerfil():
    
    idmiembro = int(request.form['txt_idmiembro'])
    cualidades = request.form['txt_cualipers']
    actitudes = request.form['txt_actiminis']
    antecedentes = request.form['txt_antecedentes']
    ministerios = request.form.getlist('ministerios')

    # Convertir ministerios a string.
    r_ministerio = ''
    for m in ministerios:
        r_ministerio += m + ','
    
    r_ministerio = r_ministerio.rstrip(',')
    
    perf = MiembroPerfilModel()
    perf.guardar(idmiembro, r_ministerio, cualidades, actitudes, antecedentes, True, None)
    
    return redirect(url_for('registrar_formulario_perfil.index_perfil'))
    

    

