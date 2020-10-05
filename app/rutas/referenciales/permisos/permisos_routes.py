from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app as app, session
from flask.json import jsonify
from app.rutas.referenciales.permisos.Form import Formulario
from app.Models.referenciales.permisos.Permiso_dao import Permiso_dao

perm = Blueprint('permisos', __name__, template_folder='templates')
titulo = 'Mantener Permisos'
title_formulario = 'Formulario Permisos'

@perm.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@perm.route('/')
def index():
    md = Permiso_dao()
    lista = md.getGrupos()
    return render_template('permisos/index.html', titulo=titulo, items=lista)

@perm.route('/eliminar/<id>')
def eliminar(id):
    md = Permiso_dao()
    res = md.eliminar(id)
    if 'codigo' not in res:
        flash('Se ha cambiado el estado exitosamente', 'success')
    elif 'codigo' in res and res['codigo'] == '23503':
        flash('El registro esta siendo utilizado en alguna otra parte.', 'danger')
    else:
        flash('Se ha borrado exitosamente el registro', 'success')
    return redirect(url_for('permisos.index'))

@perm.route('/formulario/gestionar/<id>')
def gestionar(id):
    form = Formulario()
    form.gru_id.data = id
    obj = Permiso_dao()
    data = obj.getPaginasByGrupo(int(id))
    if not data:
        flash('No pudo cargarse datos en el formulario. Contacte con el administrador', 'danger')
    elif data[0]['gru_des']:
        form.nombre_grupo.data = data[0]['gru_des']
    return render_template('permisos/formulario.html', titulo="Asignar paginas y permisos", form=form, items=data)

@perm.route('/formulario/editar_permiso/<int:id_grupo>/<int:id_pagina>')
def editarPermiso(id_grupo, id_pagina):
    form = Formulario()
    form.gru_id.data = id_grupo
    form.pag_id.data = id_pagina
    obj = Permiso_dao()
    data = obj.getPermisoById(id_pagina, id_grupo)
    if not data:
        flash('No pudo cargarse datos en el formulario. Contacte con el administrador', 'danger')
    elif data['pag_id']:
        form.nombre_pagina.data = data['pag_nombre']
        form.leer.data = data['leer']
        form.insertar.data = data['insertar']
        form.editar.data = data['editar']
        form.borrar.data = data['borrar']
    return render_template('permisos/editar_permiso.html', titulo="Editar Permiso", form=form, id=id_grupo)

@perm.route('/formulario', methods=['GET', 'POST'])
def formulario():
    # Obtener antes dats de permisos para llenar el formulario
    form = Formulario()
    #if form.id.data:
    #    del form.personas
    obj = Permiso_dao()
    res = None
    mensaje = ''
    
    if request.method == 'GET':
        return render_template('permisos/formulario.html', titulo=titulo, form=form)
    else:
        isValid = form.validate_on_submit()
        if isValid:

            next = request.args.get('next', None)
            if next:
                return redirect(next)

            id = form.id.data
            
            if not id:
                #campo_pagina = form.campo_pagina.data
                #campo_uri = form.campo_uri.data
                #mod_id = form.modulos.data
                # res = obj.guardar(mod_id, campo_pagina.capitalize(), campo_uri)
                mensaje = ['Se guardo correctamente', 'success']
            else:
                #campo_pagina = form.campo_pagina.data
                #campo_uri = form.campo_uri.data
                #mod_id = form.modulos.data
                # res = obj.modificar(campo_pagina.capitalize(), mod_id, campo_uri, id)
                mensaje = ['Se modifico correctamente', 'success']

            if res:
                flash(mensaje[0], mensaje[1])
                return redirect(url_for('permisos.index'))
            else:
                return redirect(url_for('permisos.gestionar', id=id))
        else:
            id = form.id.data
            if id:
                flash('Error en la validación, revise de vuelta', 'warning')
                return redirect(url_for('permisos.gestionar', id=id))
            flash('Error en la validación, revise de vuelta', 'warning')
            return redirect(url_for('permisos.formulario'))

## metodos con ajax
@perm.route('/get_pagina/<id>')
def getPagina(id):
    per = Permiso_dao()
    lista = per.getPaginaByModulo(id)
    return jsonify(lista)