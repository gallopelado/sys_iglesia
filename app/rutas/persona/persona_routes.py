# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Se importa el modelo Persona
from app.Models.PersonaModel import PersonaModel
# Se importa el modelo TipoPersona
from app.Models.TipoPersonaModel import TipoPersonaModel
# Se importa el helper

# Significa persona modulo, permod. 
permod = Blueprint('persona', __name__, template_folder='templates')

@permod.route('/')
def index_persona():
    """Metodo index_persona.

    Obtiene datos de PersonaModel() a traves del 
    metodo listarPersonas() para mostrar en la vista
    index de persona.

    Retorna: -- render_template()

    """
    # generar instancia
    pm = PersonaModel()
    
    # asignar lista a una variable
    items = pm.listarPersonas()
    
    return render_template('persona/index.html', items = items)

@permod.route('/frm_persona')
def frm_persona():
    """Metodo frm_persona.

    Obtiene datos de TipoPersonaModel() a traves del
    metodo listarTiposPersona() para mostrar en la vista
    frm_persona de persona.

    Retorna: -- render_template()

    """
    # generar instancia
    tpm = TipoPersonaModel()
    lista_tipos = tpm.listarTiposPersona()
    return render_template('persona/frm_persona.html',  lista_tipos = lista_tipos)

@permod.route('/guardar', methods = ['POST'])
def guardar():
    """Metodo guardar.

    Persiste datos ingresados del formulario mediante POST a
    PersonaModel(). Se analiza si la operacion es guardar o modificar.

    Retorna: -- redirect()

    """
    if request.method == "POST":

        # Recuperar datos del formulario
        idpersona = request.form['idpersona']
        cedula = request.form['txtcedula']
        tipopersona = 2
        nombres = request.form['txtnombres']
        apellidos = request.form['txtapellidos']
        obs = request.form['txtobs']

        # observar
        #print('Datos recolectados ' + str(len(idpersona)) + ', ' + cedula + ', ' + tipopersona + ', ' + nombres + ', ' + apellidos + ', ' + obs)    

        # Validar campos
        if len(cedula) > 0 and len(nombres) > 0 and len(apellidos) > 0:
            # Correcto, hacer cambios.
            # Opciones: Guardar, Modificar
            if len(idpersona) == 0:
                # Guardar
                pm = PersonaModel()
                resul = pm.guardar('a', None, cedula, nombres, apellidos, tipopersona, obs)
                flash("Exito, se guardó correctamente", "success")
                return redirect(url_for('persona.index_persona'))
            else:
                # Modificar
                pm = PersonaModel()
                pm.guardar('m', idpersona, cedula, nombres, apellidos, tipopersona, obs)
                flash("Exito, se modificó correctamente", "success")
                return redirect(url_for('persona.index_persona'))
        else:
            # No debe dejarse campos vacios. 
            flash("Error, no debe dejarse campos vacíos !", "danger")
            return False   

@permod.route('/modificar/<idpersona>')
def modificar_persona(idpersona):
    """Metodo modificar_persona.

       Busca en el modelo mediante id recibida por GET a
       PersonaModel() para devolver a la vista frm_persona.

       Parametros: 
        idpersona: --int
       Retorna: 
        --render_template() 

    """
    pm = PersonaModel()
    persona = pm.recuperaPersona(idpersona)    
    return render_template('persona/frm_persona.html', persona = persona)

@permod.route('/eliminar/<idpersona>')
def eliminar_persona(idpersona):
    """Metodo eliminar_persona.

    Eliminar mediante id por GET a un registro del modelo.

    Parametros:
        idpersona: --int

    Retorna: 
        redirect()

    """
    pm = PersonaModel()
    pm.guardar('b', idpersona, None, None, None, None, None)
    flash('Exito, se eliminó correctamente', "success")
    return redirect(url_for('persona.index_persona'))

@permod.route('/get_persona/<idpersona>')
def get_persona(idpersona):
    """Metodo get_persona.

    Genera un objeto JSON a traves de datos obtenidos del modelo.

    Parametros:
        idpersona: --int

    Retorna:
        data: --json

    """
    pm =PersonaModel()    
    data = pm.recuperaPersona(idpersona)
    return jsonify(data)