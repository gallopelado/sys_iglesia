from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app as app, session
from app.rutas.referenciales.paginas.Form import Formulario
from app.Models.referenciales.paginas.Pagina_dao import Pagina_dao

pag = Blueprint('paginas', __name__, template_folder='templates')
titulo = 'Mantener Paginas'
title_formulario = 'Formulario Paginas'

@pag.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@pag.route('/')
def index():
    md = Pagina_dao()
    lista = md.getLista()
    return render_template('paginas/index.html', titulo=titulo, items=lista)

@pag.route('/eliminar/<id>')
def eliminar(id):
    md = Pagina_dao()
    res = md.eliminar(id)
    if 'codigo' not in res:
        flash('Se ha cambiado el estado exitosamente', 'success')
    elif 'codigo' in res and res['codigo'] == '23503':
        flash('El registro esta siendo utilizado en alguna otra parte.', 'danger')
    else:
        flash('Se ha borrado exitosamente el registro', 'success')
    return redirect(url_for('paginas.index'))

@pag.route('/formulario/editar/<id>')
def editar(id):
    form = Formulario()
    obj = Pagina_dao()
    data = obj.getPaginaId(id)
    if data:
        form.id.data = data['pag_id']
        form.campo_pagina.data = data['pag_nombre']
        form.campo_uri.data = data['pag_direcc']
        form.modulos.data = data['mod_id']
    else:
        flash('No pudo cargarse datos en el formulario. Contacte con el administrador', 'danger')
    return render_template('paginas/formulario.html', titulo=title_formulario, form=form, editar=True)

@pag.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = Formulario()
    #if form.id.data:
    #    del form.personas
    obj = Pagina_dao()
    res = None
    mensaje = ''
    
    if request.method == 'GET':
        return render_template('paginas/formulario.html', titulo=titulo, form=form)
    else:
        isValid = form.validate_on_submit()
        if isValid:

            next = request.args.get('next', None)
            if next:
                return redirect(next)

            id = form.id.data
            
            if not id:
                campo_pagina = form.campo_pagina.data
                campo_uri = form.campo_uri.data
                mod_id = form.modulos.data
                res = obj.guardar(mod_id, campo_pagina.capitalize(), campo_uri)
                mensaje = ['Se guardo correctamente', 'success']
            else:
                campo_pagina = form.campo_pagina.data
                campo_uri = form.campo_uri.data
                mod_id = form.modulos.data
                res = obj.modificar(campo_pagina.capitalize(), mod_id, campo_uri, id)
                mensaje = ['Se modifico correctamente', 'success']

            if res:
                flash(mensaje[0], mensaje[1])
                return redirect(url_for('paginas.index'))
            else:
                return redirect(url_for('paginas.editar', id=id))
        else:
            id = form.id.data
            if id:
                flash('Error en la validación, revise de vuelta', 'warning')
                return redirect(url_for('paginas.editar', id=id))
            flash('Error en la validación, revise de vuelta', 'warning')
            return redirect(url_for('paginas.formulario'))
