from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json

insa = Blueprint('inscripcion_alumnos', __name__, template_folder='templates')

@insa.route('/')
def index():
    return render_template('inscripcion_alumnos/index.html')