from flask import Blueprint

nac = Blueprint("nacionalidad", __name__, template_folder='templates')

@nac.route("/")
def index_nacionalidad():
    return "Estas en Index nacionalidad"


