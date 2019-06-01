# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash
# Se importa el modelo Persona
from app.Models.PersonaModel import PersonaModel
# Se importa el modelo TipoPersona
from app.Models.TipoPersonaModel import TipoPersonaModel
# Se importa el helper

# Significa persona modulo, permod. 
permod = Blueprint('persona', __name__, template_folder='templates')

@permod.route('/')
def index_persona():
    # generar instancia
    pm = PersonaModel()
    
    # asignar lista a una variable
    items = pm.listarPersonas()
    
    return render_template('persona/index.html', items = items)

@permod.route('/frm_persona')
def frm_persona():
    # generar instancia
    tpm = TipoPersonaModel()

    lista_tipos = tpm.listarTiposPersona()
    print(lista_tipos)
    return render_template('persona/frm_persona.html',  lista_tipos = lista_tipos)

@permod.route('/guardar', methods = ['POST'])
def guardar():
    if request.method == "POST":
        #print(request.form)

        # Recuperar datos del formulario
        idpersona = request.form['idpersona']
        cedula = request.form['txtcedula']
        tipopersona = request.form['cbo_tipopersona']
        nombres = request.form['txtnombres']
        apellidos = request.form['txtapellidos']
        obs = request.form['txtobs']

        # observar
        print('Datos recolectados ' + str(len(idpersona)) + ', ' + cedula + ', ' + tipopersona + ', ' + nombres + ', ' + apellidos + ', ' + obs)    

        # Validar campos
        if len(cedula) > 0 and len(nombres) > 0 and len(apellidos) > 0:
            # Correcto, hacer cambios.
            # Opciones: Guardar, Modificar
            if len(idpersona) == 0:
                # Guardar
                pm = PersonaModel()
                resul = pm.guardar('a', None, cedula, nombres, apellidos, tipopersona, obs)
                return redirect(url_for('persona.index_persona'))
            else:
                # Modificar
                pass
        else:
            # No debe dejarse campos vacios. 
            return False   
        
        

    return "Guardando!"
