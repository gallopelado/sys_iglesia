# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Librerias para generar pdf
from flask_weasyprint import HTML, render_pdf
# Otras utilidades
from app.helps.helps import fechaActual
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


@minf.route('/listar_miembros_activos_pdf', methods=['POST'])
def listarMiembrosActivosPdf():
    titulo = 'Reporte:Listar Miembros Oficiales'
    form = FormGenerar()    
    # Recolectar datos del formulario.
    fechadesde = form.fechainicio.data if form.fechainicio.data else None
    fechahasta = form.fechainicio.data if form.fechainicio.data else None   
    requisito = form.razonalta.data if form.razonalta.data else None
    sexo = form.sexo.data if form.sexo.data else None
    civil = form.ecivil.data if form.ecivil.data else None
    mes = form.cumplemes.data if form.cumplemes.data else None
    lista = mo.listarMiembrosReport(fechadesde, fechahasta, requisito, sexo, civil, mes)
    print(lista)
    html = render_template('membresia/plantillas/listar_miembros.html', items=lista, titulo=titulo, fecha_actual=fechaActual())            
    return render_pdf(HTML(string=html))
