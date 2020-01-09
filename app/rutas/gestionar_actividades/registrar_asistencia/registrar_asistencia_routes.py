# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos
from app.Models.actividad_models.AsistenciaModel import AsistenciaModel
from app.Models.PersonaModel import PersonaModel
from app.Models.ReferencialModel import ReferencialModel
from app.helps.helps import fechaActual, fechaFormatoLargo

# Registrar modulo
asis = Blueprint('registrar_asistencia', __name__, template_folder='templates')
refm = ReferencialModel()
perm = PersonaModel()
titulo = 'Registrar asistencias de miembros de la iglesia'

@asis.route('/')
def index_asistencia():    
    return render_template('registrar_asistencia/index.html', titulo=titulo)


@asis.route('/formulario_asistencia')
def formularioAsistencia():
    evento = refm.getAll('referenciales.eventos')
    fecha = fechaFormatoLargo(fechaActual())
    persona = perm.listarPersonas()         
    return render_template('registrar_asistencia/formulario.html', titulo='Formulario Asistencia', evento=evento, fecha=fecha, persona=persona)


@asis.route('/guardar', methods=['POST'])
def guardar():
    print(request.json)
    return jsonify({'procesado':True})