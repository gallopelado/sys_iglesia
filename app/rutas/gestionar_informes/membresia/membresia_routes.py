# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Librerias para generar pdf
from flask_weasyprint import HTML, render_pdf
# Importar modelos
from app.Models.MiembroPerfilModel import MiembroOficialModel
# Importar formularios
from app.rutas.gestionar_informes.membresia.formularios import FormGenerar
# Registrar modulo.
# minf -- membresia informes
minf = Blueprint('membresia', __name__, template_folder='templates')
mo = MiembroOficialModel()

@minf.route('/')
def listarMiembrosActivos():
    titulo = 'Reporte:Listar Miembros Oficiales'
    form = FormGenerar()
    lista = mo.listarMiembros()
    return render_template('membresia/informe_listar_miembros.html', titulo=titulo, lista=lista, form=form)