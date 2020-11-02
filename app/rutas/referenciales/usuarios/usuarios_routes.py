from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app as app, session
from werkzeug.security import generate_password_hash
from app.rutas.referenciales.usuarios.Form import Formulario
from app.Models.referenciales.usuarios.Usuario_dao import Usuario_dao

usu = Blueprint('usuarios', __name__, template_folder='templates')
titulo = 'Mantener Usuarios'
title_formulario = 'Formulario Usuarios'

@usu.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@usu.route('/')
def index():
    md = Usuario_dao()
    lista = md.getLista()
    return render_template('usuarios/index.html', titulo=titulo, items=lista)

@usu.route('/eliminar/<id>')
def eliminar(id):
    md = Usuario_dao()
    res = md.darBaja(id, session['usu_id'])
    if 'codigo' not in res:
        flash('Se ha cambiado el estado exitosamente', 'success')
    elif 'codigo' in res and res['codigo'] == '23503':
        flash('El registro esta siendo utilizado en alguna otra parte.', 'danger')
    else:
        flash('Se ha borrado exitosamente el registro', 'success')
    return redirect(url_for('usuarios.index'))

@usu.route('/formulario/editar/<id>')
def editar(id):
    form = Formulario()
    obj = Usuario_dao()
    data = obj.getUsuarioId(id)
    if data:
        form.id.data = data['usu_id']
        form.nick.data = data['usu_nick']
        form.campo_funcionario.data = data['funcionario']
        form.funcionario.data = data['fun_id']
        form.grupos.data = data['gru_id']
    else:
        flash('No pudo cargarse datos en el formulario. Contacte con el administrador', 'danger')
    return render_template('usuarios/formulario.html', titulo=title_formulario, form=form, editar=True)

@usu.route('/formulario', methods=['GET', 'POST'])##modificar bien
def formulario():
    form = Formulario()
    if form.id.data:
        del form.funcionario
    obj = Usuario_dao()
    res = None
    mensaje = ''
    
    if request.method == 'GET':
        listaf = obj.getFuncionarios()
        #Debe volver a recargarse el combo por si existan nuevos registros
        form.funcionario.choices = [(item['fun_id'], item["funcionario"]) for item in listaf]
        return render_template('usuarios/formulario.html', titulo=titulo, form=form)
    else:
        isValid = form.validate_on_submit()
        if isValid:

            next = request.args.get('next', None)
            if next:
                return redirect(next)

            usu_id = session['usu_id']
            id = form.id.data
            
            if not id:
                fun_id = form.funcionario.data
                grupo_id = form.grupos.data
                nick = form.nick.data
                clave = generate_password_hash(form.clave.data, method='sha256')
                res = obj.guardar(nick, clave, fun_id, grupo_id, usu_id)
                mensaje = ['Se guardo correctamente', 'success']
            else:
                grupo_id = form.grupos.data
                nick = form.nick.data
                clave = generate_password_hash(form.clave.data, method='sha256')
                res = obj.modificar(nick, clave, grupo_id, usu_id, id)
                mensaje = ['Se modifico correctamente', 'success']

            if res:
                flash(mensaje[0], mensaje[1])
                return redirect(url_for('usuarios.index'))
            else:
                return redirect(url_for('usuarios.editar', id=id))
        else:
            id = form.id.data
            if id:
                flash('Error en la validación, revise de vuelta', 'warning')
                return redirect(url_for('usuarios.editar', id=id))
            flash('Error en la validación, revise de vuelta', 'warning')
            return redirect(url_for('usuarios.formulario'))
