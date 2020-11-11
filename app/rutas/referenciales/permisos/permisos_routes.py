from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app as app, session,abort
from flask.json import jsonify
from wtforms.form import Form
from app.rutas.referenciales.permisos.Form import Formulario
from app.Models.referenciales.permisos.Permiso_dao import Permiso_dao

perm = Blueprint('permisos', __name__, template_folder='templates')
titulo = 'Mantener Permisos'
title_formulario = 'Formulario Permisos'

@perm.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo']!='ADMIN':
        abort(403, description="Acceso prohibido")

@perm.route('/')
def index():
    md = Permiso_dao()
    lista = md.getGrupos()
    return render_template('permisos/index.html', titulo=titulo, items=lista)

@perm.route('/eliminar/<int:id_grupo>/<int:id_pagina>')
def eliminar(id_grupo, id_pagina):
    md = Permiso_dao()
    res = md.eliminar(id_grupo, id_pagina)
    if res:
        flash('Se ha cambiado el estado exitosamente', 'success')
    elif 'codigo' in res and res['codigo'] == '23503':
        flash('El registro esta siendo utilizado en alguna otra parte.', 'danger')
    else:
        flash('Se ha borrado exitosamente el registro', 'success')
    return redirect(url_for('permisos.gestionar', id=id_grupo))

@perm.route('/formulario/gestionar/<id>')
def gestionar(id):
    form = Formulario()
    form.gru_id.data = id
    obj = Permiso_dao()
    data = obj.getPaginasByGrupo(int(id))
    if not data:
        form.nombre_grupo.data = obj.getGruposId(id)['descripcion']
        flash('No existen registros para el formulario.', 'warning')
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
    # Obtener antes datos de permisos para llenar el formulario
    form = Formulario()
    obj = Permiso_dao()
    res = None
    mensaje = ''
    
    if request.method == 'GET':
        return render_template('permisos/formulario.html', titulo=titulo, form=form)
    else:
        isValid = True if (form.modulos.data and form.paginas.data) or (form.gru_id.data and form.pag_id.data) else False
        if isValid:

            next = request.args.get('next', None)
            if next:
                return redirect(next)

            gru_id = form.gru_id.data
            pag_id = form.paginas.data if form.paginas.data else form.pag_id.data
            leer = form.leer.data
            insertar = form.insertar.data
            editar = form.editar.data
            borrar = form.borrar.data

            res = obj.guardar(pag_id, gru_id, leer, insertar, editar, borrar)
            mensaje = ['Se ha procesado correctamente', 'success']

            if res == True:
                flash(mensaje[0], mensaje[1])
                return redirect(url_for('permisos.gestionar', id=gru_id))
            else:
                flash('Error al procesar. Consulte al administrador. Y si sos el administrador, hule!', 'danger')
                return redirect(url_for('permisos.gestionar', id=gru_id))
        else:
            id = form.gru_id.data
            if id:
                flash('Error en la validación, revise de vuelta', 'warning')
                return redirect(url_for('permisos.gestionar', id=id))
            flash('Error en la validación, revise de vuelta', 'warning')
            return redirect(url_for('permisos.formulario'))

## metodos con ajax
@perm.route('/get_pagina/<id>/<gru_id>')
def getPagina(id, gru_id):
    per = Permiso_dao()
    lista = per.getPaginaByModulo(id, gru_id)
    return jsonify(lista)