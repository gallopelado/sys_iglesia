# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,session,abort

# Importar modelos
from app.Models.MiembroPerfilModel import MiembroPerfilModel
from app.Models.ReferencialModel import ReferencialModel

perfil = Blueprint('registrar_formulario_perfil', __name__, template_folder='templates')

@perfil.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo'] not in ('ADMIN', 'SECRETARIA'):
        abort(403, description="Acceso prohibido")

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


@perfil.route('/ver_perfil/<int:idmiembro>', methods=['GET'])
def ver(idmiembro):

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

    return render_template('registrar_formulario_perfil/formulario_perfil.html', ministerios = ministerios, perfil = perfil, minis = minis, lista_perfil = perfil)


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
    res = perf.guardar(idmiembro, r_ministerio, cualidades, actitudes, antecedentes, True, None)
    
    # Mensaje de éxito.
    if res == True:
        flash('Se ha procesado con éxito su acción !', 'success')
        return redirect(url_for('registrar_formulario_perfil.index_perfil'))
    
    flash('Algo ha salido mal', 'warning')
    return redirect(url_for('registrar_formulario_perfil.formPerfil', idmiembro=idmiembro))


# Rutas para ajax

    

    

