# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Se importa el modelo FormularioAdmisionModel

# Se importa el modelo Persona
from app.Models.PersonaModel import PersonaModel
# Se importa el modelo Ciudad
from app.Models.CiudadModel import CiudadModel
# Se importa el modelo ClasificacionSocial
from app.Models.ClasificacionSocialModel import ClasificacionSocialModel
# Se importa el modelo Relacion Familiar
from app.Models.RelacionFamiliarModel import RelacionFamiliarModel
# Se importa el modelo Forma Contacto
from app.Models.FormaContactoModel import FormaContactoModel


# Registrar las rutas en Blueprint
formadmi = Blueprint('registrar_formulario_admision', __name__, template_folder='templates')

# Elaborar las rutas

@formadmi.route('/')
def index_formadmi():
    return "Bienvenido al index de Formulario Admision"

@formadmi.route('/frm_admi')
def frm_admi():

    lista_personas = datalistPersona()
    lista_padres = datalistPadres()
    lista_ciudades = comboCiudad()
    lista_clasi = comboClasificacionSocial()
    lista_relaciones = comboRelaciones()
    lista_formas = comboFormaContacto()
    
    return render_template('registrar_formulario_admision/frm_admision.html', lista_personas = lista_personas, lista_padres = lista_padres,
    lista_ciudades = lista_ciudades, lista_clasi = lista_clasi, lista_relaciones = lista_relaciones,
    lista_formas = lista_formas)

# Funciones operativas

def datalistPersona():
    """Funcion datalistPersona.

    Busca en el modelo todas las personas, convierte los resultados
    a cadena, en formato del componente html datalist.

    """
    # Se procesan datos para el datalist
    pm = PersonaModel()
    lista = pm.recuperaPersonas()    
    combo = ""
    for x in lista:        
        combo += "<option value='" + str(x[0]) +  "'>Id:" + str(x[0]) + " - " + str(x[2]) + " " + str(x[3]) + "</option>"    
    return combo

def datalistPadres():
    """Funcion datalistPadres.

    Busca en el modelo todas las personas, convierte los resultados
    a cadena, en formato del componente html datalist.

    """
    # Se procesan datos para el datalist
    pm = PersonaModel()
    lista = pm.recuperaPersonas()    
    combo = ""
    for x in lista:        
        combo += "<option value='" + str(x[2]) + " " + str(x[3]) +  "'>"    
    return combo

def comboCiudad():
    cm = CiudadModel()
    lista = cm.listarTodos()
    combo = ""
    for ciudad in lista:
        combo += "<option value='" + str(ciudad[0]) + "'>" + str(ciudad[1]) + "</option>\n"
    return combo

def comboClasificacionSocial():
    clsm = ClasificacionSocialModel()
    lista = clsm.obtenerClasificaciones()
    combo = ""
    for item in lista:
        combo += "<option value='" + str(item[0]) + "'>" + str(item[1]) + "</option>\n"
    return combo

def comboRelaciones():
    rfm = RelacionFamiliarModel()
    lista = rfm.obtenerRelaciones()
    combo = ""
    for item in lista:
        combo += "<option value='" + str(item[0]) + "'>" + str(item[1]) + "</option>\n"
    return combo

def comboFormaContacto():
    focm = FormaContactoModel()
    lista = focm.obtenerFormas()
    combo = ""
    for item in lista:
        combo += "<option value='" + str(item[0]) + "'>" + str(item[1]) + "</option>\n"
    return combo