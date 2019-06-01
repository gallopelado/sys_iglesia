from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.Models.CiudadModel import CiudadModel
from app.helps.helps import limpiar_campo

# Se modularizan las vistas de ciudades.
mod = Blueprint("ciudad", __name__, template_folder="templates")

@mod.route("/")
def index_ciudad():
    cm = CiudadModel()
    items = cm.listarTodos()    
    print(items)
    return render_template('ciudad/index.html', items = items)

@mod.route("/frm_ciudad")
def frm_ciudad():
    return render_template('ciudad/frm_ciudad.html')

@mod.route("/guardar", methods = ["POST"])
def guardar_ciudad():
    if request.method == "POST":
        descripcion = request.form["txtdescripcion"]
        descripcion = limpiar_campo(descripcion)                
        if descripcion != "" and descripcion != None and len(descripcion) != 0:
            cm = CiudadModel()
            resul = cm.guardar(descripcion)
            if resul == True:
                flash("Exito, se salvo correctamente", "success")
                return redirect(url_for('ciudad.index_ciudad'))
            else:
                flash(resul, "danger")
                return redirect(url_for('ciudad.index_ciudad'))                            
        else:
            flash("Error, el campo no puede estar vacio", "danger")
            return redirect(url_for('ciudad.index_ciudad'))
    