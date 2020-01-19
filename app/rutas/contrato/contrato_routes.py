from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

contr = Blueprint("contrato", __name__, template_folder="templates")
titulo = 'Mantener Contratos'

@contr.route('/')
def indexMantenerContrato():
    return render_template('contrato/index.html', titulo=titulo)

@contr.route('/formulario')
def formularioMantenerContrato():
    titulo = 'Formulario Mantener Contrato'
    return render_template('contrato/formulario.html', titulo=titulo)