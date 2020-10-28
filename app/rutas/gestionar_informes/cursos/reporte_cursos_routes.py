# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
# Librerias para generar pdf
from flask_weasyprint import HTML, render_pdf
# Otras utilidades
from app.helps.helps import fechaActual
# Importar formularios
from app.rutas.gestionar_informes.actividades.FormListaActividadesAnuales import FormListaActividadesAnuales

r_cur = Blueprint('r_cursos', __name__, template_folder='templates')

@r_cur.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@r_cur.route('/')
def mostrarFormularioMalla():
    from app.Models.gestionar_cursos.malla_curricular.MallaCurricular_dao import MallaCurricular_dao
    from app.rutas.gestionar_informes.cursos.FormMalla import FormMalla
    titulo = 'Reporte:Listar Malla Curricular'
    form = FormMalla()
    md = MallaCurricular_dao()
    lista_malla = md.obtenerMallaCurricular()
    form.malla.choices = [ (item['idmalla'], item['anho_des']) for item in lista_malla ]
    
    malla_id = None
    for item in lista_malla:
        if item['estado'] == 'ACTIVO':
            malla_id = item['idmalla']

    lista_cursos = md.obtenerCursosRegistrados(malla_id)
    return render_template('cursos/informe_listar_malla.html', titulo=titulo, lista=lista_cursos, form=form)

@r_cur.route('/listar_malla_pdf', methods=['POST'])
def listarMallaPdf():
    from app.Models.gestionar_cursos.malla_curricular.MallaCurricular_dao import MallaCurricular_dao
    from app.rutas.gestionar_informes.cursos.FormMalla import FormMalla
    titulo = 'Reporte:Listar Malla Curricular'
    form = FormMalla()
    malla_id = form.malla.data
    md = MallaCurricular_dao()
    lista_malla = md.obtenerCursosRegistrados(malla_id)
    html = render_template('cursos/plantillas/listar_malla.html', items=lista_malla, titulo=titulo, fecha_actual=fechaActual())
    return render_pdf(HTML(string=html))