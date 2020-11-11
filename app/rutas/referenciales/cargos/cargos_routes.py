from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app as app, session,abort
from app.rutas.referenciales.motivo_desercion.Form import Formulario
from app.Models.referenciales.cargos.Cargos_dao import Cargos_dao

car = Blueprint('cargos', __name__, template_folder='templates')
titulo = 'Mantener Cargos'
title_formulario = 'Formulario Cargos'

@car.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo']!='ADMIN':
        abort(403, description="Acceso prohibido")

@car.route('/')
def index():
    md = Cargos_dao()
    lista = md.getLista()
    return render_template('cargos/index.html', titulo=titulo, items=lista)

@car.route('/eliminar/<id>')
def eliminar(id):
    md = Cargos_dao()
    res = md.eliminar(id)
    if res:
        flash('Se ha borrado exitosamente el registro', 'success')
    elif 'codigo' in res and res['codigo'] == '23503':
        flash('El registro esta siendo utilizado en alguna otra parte.', 'danger')
    else:
        flash('Se ha borrado exitosamente el registro', 'success')
    return redirect(url_for('cargos.index'))

@car.route('/formulario/editar/<id>')
def editar(id):
    form = Formulario()
    md = Cargos_dao()
    data = md.getCursoId(id)
    if data:
        form.usu_id.data = session['usu_id']
        form.id.data = data['id']
        form.descripcion.data = data['descripcion']
    else:
        flash('No pudo cargarse datos en el formulario. Contacte con el administrador', 'danger')
    return render_template('cargos/formulario.html', titulo=title_formulario, form=form)

@car.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = Formulario()
    md = Cargos_dao()
    res = None
    mensaje = ''
    if request.method == 'GET':
        form.usu_id.data = session['usu_id']
        return render_template('cargos/formulario.html', titulo=titulo, form=form)
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
                return redirect(url_for('cargos.index'))
            else:
                return redirect(url_for('cargos.editar', id=id, titulo=titulo))
        else:
            flash('Error en la validación, revise de vuelta', 'warning')
            return redirect(url_for('cargos.index'))
