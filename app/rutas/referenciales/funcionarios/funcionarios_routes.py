from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app as app, session, abort
from app.rutas.referenciales.funcionarios.Form import Formulario
from app.Models.referenciales.funcionarios.Funcionario_dao import Funcionario_dao

fun = Blueprint('funcionarios', __name__, template_folder='templates')
titulo = 'Mantener Funcionarios'
title_formulario = 'Formulario Funcionario'

@fun.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo']!='ADMIN':
        abort(403, description="Acceso prohibido")

@fun.route('/')
def index():
    md = Funcionario_dao()
    lista = md.getLista()
    return render_template('funcionarios/index.html', titulo=titulo, items=lista)

@fun.route('/eliminar/<id>')
def eliminar(id):
    md = Funcionario_dao()
    res = md.eliminar(id, session['usu_id'])
    if 'codigo' not in res:
        flash('Se ha cambiado el estado exitosamente', 'success')
    elif 'codigo' in res and res['codigo'] == '23503':
        flash('El registro esta siendo utilizado en alguna otra parte.', 'danger')
    else:
        flash('Se ha borrado exitosamente el registro', 'success')
    return redirect(url_for('funcionarios.index'))

@fun.route('/formulario/editar/<id>')
def editar(id):
    form = Formulario()
    obj = Funcionario_dao()
    data = obj.getFuncionarioId(id)
    if data:
        form.id.data = data['fun_id']
        form.campo_persona.data = data['funcionario']
        form.personas.data = data['fun_id']
        form.cargos.data = data['car_id']
    else:
        flash('No pudo cargarse datos en el formulario. Contacte con el administrador', 'danger')
    return render_template('funcionarios/formulario.html', titulo=title_formulario, form=form, editar=True)

@fun.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = Formulario()
    if form.id.data:
        del form.personas
    obj = Funcionario_dao()
    res = None
    mensaje = ''
    
    if request.method == 'GET':
        listap = [ (item['per_id'], item['persona']) for item in obj.getPersonas(2) ]
        listap.insert(0, (000,'...'))
        form.personas.choices = listap
        return render_template('funcionarios/formulario.html', titulo=titulo, form=form)
    else:
        isValid = form.validate_on_submit()
        if isValid:

            next = request.args.get('next', None)
            if next:
                return redirect(next)

            usu_id = session['usu_id']
            id = form.id.data
            
            if not id:
                fun_id = form.personas.data
                if not fun_id or fun_id == 000:
                    flash('Debe escoger un funcionario', 'danger')
                    return redirect(url_for('funcionarios.index'))
                car_id = form.cargos.data
                res = obj.guardar(fun_id, car_id, usu_id)
                mensaje = ['Se guardo correctamente', 'success']
            else:
                car_id = form.cargos.data
                res = obj.modificar(id, car_id, usu_id)
                mensaje = ['Se modifico correctamente', 'success']

            if res:
                flash(mensaje[0], mensaje[1])
                return redirect(url_for('funcionarios.index'))
            else:
                return redirect(url_for('funcionarios.editar', id=id))
        else:
            id = form.id.data
            if id:
                flash('Error en la validación, revise de vuelta', 'warning')
                return redirect(url_for('funcionarios.editar', id=id))
            flash('Error en la validación, revise de vuelta', 'warning')
            return redirect(url_for('funcionarios.formulario'))
