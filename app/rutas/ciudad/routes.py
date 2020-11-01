from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,session
from app.Models.CiudadModel import CiudadModel
from app.helps.helps import limpiar_campo

# Se modularizan las vistas de ciudades.
mod = Blueprint("ciudad", __name__, template_folder="templates")

@mod.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))

@mod.route("/")
def index_ciudad():
    cm = CiudadModel()
    items = cm.listarTodos()        
    return render_template('ciudad/index.html', items = items)

@mod.route("/frm_ciudad")
def frm_ciudad():
    return render_template('ciudad/frm_ciudad.html')

@mod.route("/guardar", methods = ["POST"])
def guardar_ciudad():
    
    # Comprobar si el metodo utilizado es POST.
    if request.method == "POST":
        
        # Recolectar datos del formulario.
        idciudad =  request.form["idciudad"]
        descripcion = request.form["txtdescripcion"]
        descripcion = limpiar_campo(descripcion)
        
        # Comprobar si el campo idciudad esta cargado.
        if len(idciudad) > 0:
            
            # Modificar
            if descripcion != "" and descripcion != None and len(descripcion) != 0:
                cm = CiudadModel()
                resul = cm.modificar(idciudad, descripcion)
                if resul == True:
                    flash("Exito, se salvo correctamente", "success")
                    return redirect(url_for('ciudad.index_ciudad'))
                else:
                    flash(resul, "danger")
                    return redirect(url_for('ciudad.index_ciudad'))                            
            else:
                flash("Error, el campo no puede estar vacio", "danger")
                return redirect(url_for('ciudad.index_ciudad'))


        else:

            # Guardar
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

    else:
        return "Error en la peticion"

@mod.route('/modificar/<int:idciudad>')
def modificar_ciudad(idciudad):

    cm = CiudadModel()
    datos = cm.recuperaCiudad(idciudad)

    return render_template('ciudad/frm_ciudad.html', datos = datos)

@mod.route('eliminar/<idciudad>')
def eliminar_ciudad(idciudad):

    cm = CiudadModel()
    res = cm.eliminar(idciudad)
    
    if res == True:
        flash("Se elimino correctamente", "success")
        return redirect(url_for('ciudad.index_ciudad'))
    else:
        flash(res, "warning")
        return redirect(url_for('ciudad.index_ciudad'))

@mod.route('/listar_ciudades')
def listar_ciudades():
    cm = CiudadModel()
    items = cm.listarTodos()
    print(items)    
    return jsonify({"data":items})
