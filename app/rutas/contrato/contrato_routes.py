from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,session,abort
# Importar modelos
from app.Models.ContratoModel import Contrato
from app.Models.ReferencialModel import ReferencialModel

contr = Blueprint("contrato", __name__, template_folder="templates")
titulo = 'Mantener Contratos'
conm = Contrato()
refm = ReferencialModel()

@contr.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo'] not in ('ADMIN', 'PASTOR', 'SECRETARIA'):
        abort(403, description="Acceso prohibido")

@contr.route('/')
def indexMantenerContrato():    
    lista = conm.obtenerContratos()    
    return render_template('contrato/index.html', titulo=titulo, lista=lista)

@contr.route('/formulario')
def formularioMantenerContrato():
    titulo = 'Formulario Mantener Contrato'
    tipos = refm.getAll('referenciales.tipo_contrato')        
    return render_template('contrato/formulario.html', titulo=titulo, tipos=tipos, ver=False, contrato=None)


@contr.route('/formulario/<int:id>')
def editarContrato(id):
    titulo = 'Editar Contrato'    
    tipos = refm.getAll('referenciales.tipo_contrato')    
    contrato = conm.obtenerContratosId(id)
    if contrato:        
        return render_template('contrato/formulario.html', titulo=titulo, tipos=tipos, contrato=contrato, ver=False, idcontrato=id)
    else:
        flash('No existe ese contrato.', 'danger')
        return redirect(url_for('contrato.indexMantenerContrato'))


@contr.route('/formulario/ver/<int:id>')
def verContrato(id):
    titulo = 'Ver Contrato'    
    tipos = refm.getAll('referenciales.tipo_contrato')    
    contrato = conm.obtenerContratosId(id)
    if contrato:        
        return render_template('contrato/formulario.html', titulo=titulo, tipos=tipos, contrato=contrato, ver=True, idcontrato=id)
    else:
        flash('No existe ese contrato.', 'danger')
        return redirect(url_for('contrato.indexMantenerContrato'))



@contr.route('/guardar', methods=['POST'])
def guardar():
    idcontrato = request.json['idcontrato']
    titulo = request.json['titulo']
    tipo = request.json['tipo']
    plantilla = request.json['plantilla']
    
    if idcontrato == '':        
        res = conm.guardar(titulo, tipo, plantilla)
        if res==True:
            flash('Se ha procesado correctamente', 'success')
        else:
            flash('Hubo un problema', 'danger')
        return jsonify({'estado':res if res==True else res})
    else:        
        res = conm.modificar(idcontrato, titulo, tipo, plantilla)
        if res==True:
            flash('Se ha procesado correctamente', 'success')
        else:
            flash('Hubo un problema en la operacion', 'danger')
        return jsonify({'estado':res if res==True else res})


@contr.route('/eliminar/<int:id>', methods=['GET'])
def eliminar(id):
    res = conm.eliminar(id)
    if res==True:
        flash('Se ha procesado correctamente', 'success')
        return redirect(url_for('contrato.indexMantenerContrato'))
    else:
        flash('Hubo un problema en la operacion', 'danger')
        return redirect(url_for('contrato.indexMantenerContrato'))