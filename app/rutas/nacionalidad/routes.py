from flask import Blueprint

mod = Blueprint("nacionalidad", __name__)

@mod.route("/index")
def index_nacionalidad():
    return "Estas en Index nacionalidad"