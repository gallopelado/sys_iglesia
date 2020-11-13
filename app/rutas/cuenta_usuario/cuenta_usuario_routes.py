from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json, session,abort
from app.Models.seguridad.cuenta_usuario.CuentaUsuario_dao import CuentaUsuario_dao

cu = Blueprint('cuenta_usuario', __name__, template_folder='templates')

@cu.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))

@cu.route('/userinfo')
def index():
    cum = CuentaUsuario_dao()
    data = cum.getUserData(session['usu_id'])
    return render_template('cuenta_usuario/userinfo.html', titulo='Acerca del ti', data=data)