# Se importan las librerias basicas
import time
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Librerias para generar pdf
from flask_weasyprint import HTML, render_pdf

# Importar modelos.
from app.Models.PersonaModel import PersonaModel

# Registrar modulo.
ms = Blueprint('mantenimiento_seguridad', __name__, template_folder='templates')
# fecha actual
localtime = time.localtime(time.time())
fecha_actual = f'{localtime.tm_mday}-{localtime.tm_mon}-{localtime.tm_year}'

# Referenciales
@ms.route('/')
def listarTodasPersonas():
    titulo = 'Reporte:Listar todas las personas'
    p = PersonaModel()
    lista = p.listarPersonas()
    html = render_template('mantenimiento_seguridad/informe_listar_todas_personas.html', items=lista, titulo=titulo)
    return html

@ms.route('/personas_pdf')
def personasPdf():
    titulo = 'Reporte:Listar todas las personas'
    mensaje = 'Reporte actual de personas\n registradas en el sistema'
    p = PersonaModel()
    lista = p.listarPersonas()
    html = render_template('mantenimiento_seguridad/plantillas/listar_todas_personas.html', items=lista, titulo=titulo, fecha_actual=fecha_actual, mensaje=mensaje)
    return render_pdf(HTML(string=html))

