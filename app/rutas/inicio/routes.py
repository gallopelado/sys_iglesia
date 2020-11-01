from flask import Blueprint, render_template, url_for, session, redirect

mod = Blueprint('inicio', __name__, template_folder='templates')

@mod.route("/")
def index():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('inicio/index.html')