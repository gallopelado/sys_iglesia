# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session

# Importar modelo

# Importar Modelo de Admision
from app.Models.FormAdmisionModel import FormAdmisionModel

# Importar Modelo MiembroOficialModel.
from app.Models.MiembroOficialModel import MiembroOficialModel

# Importar tipos de persona
#from app.Models.TipoPersonaModel import TipoPersonaModel

# Registrar las rutas en Blueprint
mieofi = Blueprint('registrar_miembro_oficial', __name__, template_folder='templates')

@mieofi.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

# Index.
@mieofi.route('/')
def index_mieofi():

    # Obtener miembros
    m = MiembroOficialModel()
    lista = m.listarMiembros()
    return render_template('registrar_miembro_oficial/index.html', lista = lista)



# Formulario principal.
@mieofi.route('/frm_miembro')
def frmMiembro():
    return render_template('registrar_miembro_oficial/formulario_miembro.html')



# Para editar.
@mieofi.route('/frm_miembro/<int:idmiembro>', methods=['GET'])
def frmModificar(idmiembro):
    #print(f'Parametro Recibido :{idmiembro}')
    m = MiembroOficialModel()
    lista = m.getMiembroById(idmiembro)
    
    return render_template('registrar_miembro_oficial/formulario_miembro.html', miembro = lista)



# Vista para dados de baja.
@mieofi.route('/dados_baja')
def dadosBaja():

    m = MiembroOficialModel()
    lista = m.getMiembrosDadosDeBaja()    

    return render_template('registrar_miembro_oficial/dadosbaja.html', miembros = lista)


@mieofi.route('/ver_miembro/<int:idmiembro>', methods=['GET'])
def verMiembro(idmiembro):
    m = MiembroOficialModel()
    lista = m.getMiembroById(idmiembro)

    return render_template('registrar_miembro_oficial/ver.html', miembro=lista)

################################## Rutas para AJAX.
@mieofi.route('/personas_activas')
def personasActivas():

    adm = FormAdmisionModel()
    lista = adm.getAdmisionesActivas(True)
    
    return jsonify(lista[0][0])
    

@mieofi.route('/guardar', methods=['POST'])
def guardar():
    
    # Procesar variables
    idmiembro = request.json['idmiembro']
    razonaltaid = request.json['idrazonalta']
    fechaconversion = request.json['fechaconversion']
    fechabautismo = request.json['fechabautismo']
    estadomembresia = request.json['estadomembresia']
    lugarbautismo = request.json['lugarbautismo']
    oficiador = request.json['ministro']
    fechainiciomembresia = request.json['fechainiciomembresia']
    bautizadoeniglesia = request.json['fuebautizado']
    padresmiembros = request.json['padreseniglesia']
    recibioes = request.json['recibioes']
    obs = request.json['observacion']


    # Enviar al Modelo.
    m = MiembroOficialModel()
    res = m.guardar(idmiembro, razonaltaid, fechaconversion, fechabautismo,
              lugarbautismo, oficiador, fechainiciomembresia, estadomembresia,
              bautizadoeniglesia, padresmiembros, recibioes, obs,
              0)
    if res:
        return jsonify({"guardado":True})
    
    return jsonify({"guardado": False})


@mieofi.route('/modificar', methods=['POST'])
def modificar():

    # Procesar variables
    idmiembro = request.json['idmiembro']
    razonaltaid = request.json['idrazonalta']
    fechaconversion = request.json['fechaconversion']
    fechabautismo = request.json['fechabautismo']
    estadomembresia = request.json['estadomembresia']
    lugarbautismo = request.json['lugarbautismo']
    oficiador = request.json['ministro']
    fechainiciomembresia = request.json['fechainiciomembresia']
    bautizadoeniglesia = request.json['fuebautizado']
    padresmiembros = request.json['padreseniglesia']
    recibioes = request.json['recibioes']
    obs = request.json['observacion']

    # Enviar al Modelo.
    m = MiembroOficialModel()
    res = m.modificar(idmiembro, razonaltaid, fechaconversion, fechabautismo,
                    lugarbautismo, oficiador, fechainiciomembresia, estadomembresia,
                    bautizadoeniglesia, padresmiembros, recibioes, obs,
                    0)
    if res:
        return jsonify({"guardado": True})

    return jsonify({"guardado": False})


@mieofi.route('/reincorporar', methods=['POST'])
def reincorporar():
    print(f'Recibido: {request.json}')

    idmiembro = request.json['idmiembro']
    obs = request.json['obs']

    # Generar instancia.
    m = MiembroOficialModel()
    res = m.reincorporarMiembro(idmiembro, obs)

    if res:
        return jsonify({'procesado': True})
    else:
        return jsonify({'procesado': False})
