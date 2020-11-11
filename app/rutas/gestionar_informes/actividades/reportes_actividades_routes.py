# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session,abort
# Librerias para generar pdf
from flask_weasyprint import HTML, render_pdf
# Otras utilidades
from app.helps.helps import fechaActual
# Importar formularios
from app.rutas.gestionar_informes.actividades.FormListaActividadesAnuales import FormListaActividadesAnuales

r_act = Blueprint('r_actividades', __name__, template_folder='templates')

@r_act.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo'] not in ('ADMIN', 'PASTOR'):
        abort(403, description="Acceso prohibido")

@r_act.route('/')
def mostrarFormularioActividadAnual():
    from app.Models.actividad_models.ActividadAnualModel import ActividadAnualModel
    titulo = 'Reporte:Listar Actividades Anuales'
    form = FormListaActividadesAnuales()
    an = ActividadAnualModel()
    lista_organizadores = an.getOrganizadores()
    lista_organizadores.insert(0, {'min_id':'', 'min_des':'...'})
    lista_lugares = an.getLugares()
    lista_lugares.insert(0, {'lug_id':'', 'lug_des':'...'})
    form.organizador.choices = [ (item['min_id'], item['min_des']) for item in lista_organizadores ]
    form.lugar.choices = [ (item['lug_id'], item['lug_des']) for item in lista_lugares ]
    lista_actividades = an.getListaActividadesAnhoActivo(None, None, None, None)
    return render_template('actividades/informe_listar_actividades_anuales.html', titulo=titulo, lista=lista_actividades, form=form)

@r_act.route('/form_lista_reservas')
def mostrarFormularioReservas():
    from app.Models.actividad_models.ReservaModel import ReservaModel
    from app.rutas.gestionar_informes.actividades.FormListaReserva import FormListaReserva
    titulo = 'Reporte:Listar Reservas'
    form = FormListaReserva()
    rm = ReservaModel()
    lista_reservas = rm.getReservasByParameters(None, None, None)
    return render_template('actividades/informe_listar_reservas.html', titulo=titulo, lista=lista_reservas, form=form)

@r_act.route('/listar_reservas_pdf', methods=['POST'])
def listarReservasPdf():
    from app.Models.actividad_models.ReservaModel import ReservaModel
    from app.rutas.gestionar_informes.actividades.FormListaReserva import FormListaReserva
    titulo = 'Reporte:Listar Reservas'
    form = FormListaReserva()
    estado = form.estado.data
    fechadesde = form.fechadesde.data
    fechahasta = form.fechahasta.data
    form = FormListaReserva()
    rm = ReservaModel()
    lista_reservas = rm.getReservasByParameters(estado, fechadesde, fechahasta)
    html = render_template('actividades/plantillas/listar_reservas.html', items=lista_reservas, titulo=titulo, fecha_actual=fechaActual())
    return render_pdf(HTML(string=html))

@r_act.route('/listar_actividades_anuales_pdf', methods=['POST'])
def listarActividadesAnualesPdf():
    from app.Models.actividad_models.ActividadAnualModel import ActividadAnualModel
    titulo = 'Reporte:Listar Actividades Anuales'
    form = FormListaActividadesAnuales()
    organizador = form.organizador.data
    lugar = form.lugar.data
    fechadesde = form.fechadesde.data
    fechahasta = form.fechahasta.data
    an = ActividadAnualModel()
    lista_actividades = an.getListaActividadesAnhoActivo(organizador, lugar, fechadesde, fechahasta)
    html = render_template('actividades/plantillas/listar_actividades_anuales.html', items=lista_actividades, titulo=titulo, fecha_actual=fechaActual())
    return render_pdf(HTML(string=html))