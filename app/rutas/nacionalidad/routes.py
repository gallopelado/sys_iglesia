from flask import Blueprint, session, redirect, url_for, abort

nac = Blueprint("nacionalidad", __name__, template_folder='templates')

@nac.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo'] not in ('ADMIN'):
        abort(403, description="Acceso prohibido")

@nac.route("/")
def index_nacionalidad():
    return "Estas en Index nacionalidad"


