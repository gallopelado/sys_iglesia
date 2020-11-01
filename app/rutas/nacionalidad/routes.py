from flask import Blueprint, session, redirect, url_for

nac = Blueprint("nacionalidad", __name__, template_folder='templates')

@nac.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@nac.route("/")
def index_nacionalidad():
    return "Estas en Index nacionalidad"


