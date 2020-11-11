# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session,abort
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

@minf.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo'] not in ('ADMIN', 'PASTOR'):
        abort(403, description="Acceso prohibido")

@minf.route('/')
def listarMiembrosActivos():
    titulo = 'Reporte:Listar Miembros Oficiales'
    form = FormGenerar()
    lista = mo.listarMiembros()
    return render_template('membresia/informe_listar_miembros.html', titulo=titulo, lista=lista, form=form)

@minf.route('/form_reporte_lista_obreros_comite')
def listarObrerosComite():
    from app.rutas.gestionar_informes.membresia.FormListaObrero import FormListaObrero
    from app.Models.ObreroModel import ObreroModel
    titulo = 'Reporte:Listar Obreros por comite'
    form = FormListaObrero()
    obm = ObreroModel()
    lista = obm.getListaObrerosByComite(None, None, None, None, None)
    lista_comites = obm.getListaComites()
    lista_comites.insert(0, ({'min_id':'', 'min_des':'...'}))
    form.comites.choices = [ (item['min_id'], item['min_des']) for item in lista_comites ]
    return render_template('membresia/informe_listar_obreros_comite.html', titulo=titulo, lista=lista, form=form)


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
    html = render_template('membresia/plantillas/listar_miembros.html', items=lista, titulo=titulo, fecha_actual=fechaActual())            
    return render_pdf(HTML(string=html))

@minf.route('/listar_lista_obreros_comite_pdf', methods=['POST'])
def listarObrerosComitePdf():
    from app.rutas.gestionar_informes.membresia.FormListaObrero import FormListaObrero
    from app.Models.ObreroModel import ObreroModel
    titulo = 'Reporte:Listar Obreros por comite'
    form = FormListaObrero()
    obm = ObreroModel()
    comite = form.comites.data
    fechadesde = form.fechadesde.data
    fechahasta = form.fechahasta.data
    entrenamiento = form.entrenamiento.data
    estado = form.estado.data
    lista = obm.getListaObrerosByComite(comite, fechadesde, fechahasta, entrenamiento, estado)
    html = render_template('membresia/plantillas/listar_obreros_comite.html', items=lista, titulo=titulo, fecha_actual=fechaActual())            
    return render_pdf(HTML(string=html))
