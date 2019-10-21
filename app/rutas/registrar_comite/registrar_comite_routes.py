# Se importan las librerías básicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar clase del formulario
from app.rutas.registrar_comite.formularioComite import FormularioComite

# Importar modelo

# Registrar en Blueprint
comi = Blueprint('registrar_comite', __name__, template_folder='templates')
titulo = 'Registrar Comité'

# Rutas
@comi.route('/')
def index_comite():
    return render_template('registrar_comite/index.html', titulo=titulo)

@comi.route('/formulario', methods=['GET'])
def formulario():
    titulo = 'Formulario Comité'
    form = FormularioComite()    
    return render_template('registrar_comite/formulario_comite.html', titulo=titulo, form=form)


@comi.route('/formulario', methods=['POST'])
def guardarForm():
    titulo = 'Formulario Comité'
    form = FormularioComite()
    if form.validate_on_submit():
        print(request.form)
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index_comite'))
    return render_template('registrar_comite/formulario_comite.html', titulo=titulo, form=form)