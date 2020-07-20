from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.rutas.gestionar_cursos.inscripcion_alumnos.InscripcionAlumnoServices import InscripcionAlumnoServices
asial = Blueprint('asistencia_alumnos', __name__, template_folder='templates')

@asial.route('/')
def index():
    return render_template('asistencia_alumnos/index.html', titulo="Registrar asistencia de alumnos")