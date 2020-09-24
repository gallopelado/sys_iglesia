from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app as app, session
from app.rutas.referenciales.motivo_desercion.Form import Formulario
from app.Models.referenciales.clasificacion_social.ClasificacionSocial_dao import ClasificacionSocial_dao

cls = Blueprint('clasi_social', __name__, template_folder='templates')
titulo = 'Mantener Clasificacion Social'
title_formulario = 'Formulario Clasificacion Social'

@cls.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@cls.route('/')
def index():
    md = ClasificacionSocial_dao()
    lista = md.getLista()
    return render_template('clasificacion_social/index.html', titulo=titulo, items=lista)

@cls.route('/eliminar/<id>')
def eliminar(id):
    md = ClasificacionSocial_dao()
    res = md.eliminar(id)
    if 'codigo' not in res:
        flash('Se ha borrado exitosamente el registro', 'success')
    elif 'codigo' in res and res['codigo'] == '23503':
        flash('El registro esta siendo utilizado en alguna otra parte.', 'danger')
    else:
        flash('Se ha borrado exitosamente el registro', 'success')
    return redirect(url_for('clasi_social.index'))

@cls.route('/formulario/editar/<id>')
def editar(id):
    form = Formulario()
    md = ClasificacionSocial_dao()
    data = md.getCursoId(id)
    if data:
        form.usu_id.data = session['usu_id']
        form.id.data = data['id']
        form.descripcion.data = data['descripcion']
    else:
        flash('No pudo cargarse datos en el formulario. Contacte con el administrador', 'danger')
    return render_template('clasificacion_social/formulario.html', titulo=title_formulario, form=form)

@cls.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = Formulario()
    md = ClasificacionSocial_dao()
    res = None
    mensaje = ''
    if request.method == 'GET':
        form.usu_id.data = session['usu_id']
        return render_template('clasificacion_social/formulario.html', titulo=titulo, form=form)
    else:
        isValid = form.validate_on_submit()
        if isValid:

            next = request.args.get('next', None)
            if next:
                return redirect(next)

            usu_id = form.usu_id.data
            id = form.id.data
            descripcion = (form.descripcion.data.strip()).upper()
            
            if not id:
                res = md.guardar(descripcion, usu_id)
                mensaje = ['Se guardo correctamente', 'success']
            else:
                res = md.modificar(id, descripcion, usu_id)
                mensaje = ['Se modifico correctamente', 'success']

            if res:
                flash(mensaje[0], mensaje[1])
                return redirect(url_for('clasi_social.index'))
            else:
                return redirect(url_for('clasi_social.editar', id=id, titulo=titulo))

