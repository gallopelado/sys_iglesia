from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

deser = Blueprint('desercion_alumnos', __name__, template_folder='templates')

@deser.route('/')
def index():
    return render_template('desercion_alumnos/index.html', titulo='Registrar Deserción de alumnos')