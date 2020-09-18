from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json

jusa = Blueprint('justificativo_alumno', __name__, template_folder='templates')

@jusa.route('/')
def index():
    return render_template('justificativo_alumnos/index.html', titulo='Registrar Justificativos de Ausencia')

@jusa.route('/lista_alumnos')
def listaAlumnos():
    return render_template('justificativo_alumnos/lista_alumnos.html', titulo='Lista de Alumnos')

@jusa.route('/formulario_ausencia')
def formularioAusencia():
    return render_template('justificativo_alumnos/formulario_ausencia.html', titulo='Formulario Ausencia')

@jusa.route('/lista_justificativos_alumnos')
def listaJustificativoAlumno():
    return render_template('justificativo_alumnos/lista_justificativos_alumnos.html', titulo='Lista de Justificativos por alumno')