# Se importan las librerías básicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar clase del formulario
from app.rutas.registrar_comite.formularioComite import FormularioComite

# Importar modelo
from app.Models.ComiteModel import ComiteModel

# Registrar en Blueprint
comi = Blueprint('registrar_comite', __name__, template_folder='templates')
titulo = 'Registrar Comité'
tituloForm = 'Formulario Comité'

# Generar instancia
cm = ComiteModel()

# Rutas
@comi.route('/')
def index_comite():
    lista = cm.traerTodos()
    return render_template('registrar_comite/index.html', titulo=titulo, lista=lista)

@comi.route('/formulario', methods=['GET'])
def formulario():
    form = FormularioComite()    
    return render_template('registrar_comite/formulario_comite.html', titulo=tituloForm, form=form)


@comi.route('/formulario/<int:idcomite>', methods=['GET'])
def formularioModificar(idcomite):    
    # Clase del formulario.
    form = FormularioComite()    
    datos = cm.traerPorId(idcomite)
    # Setear campos
    form.idcomite.data = datos[0] if datos else ''
    form.comite.data = datos[1] if datos else ''
    form.idlider.data = datos[2] if datos else ''
    form.lider.data = datos[3] if datos else ''
    form.idsuplente.data = datos[4] if datos else ''
    form.suplente.data = datos[5] if datos else ''
    form.descripcion.data = datos[6] if datos else ''
    form.observacion.data = datos[7] if datos else ''
    print(datos)    
    return render_template('registrar_comite/formulario_comite.html', titulo=tituloForm, form=form, datos=datos)


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