# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Se importa el modelo FormularioAdmisionModel
from app.Models.FormAdmisionModel import FormAdmisionModel
# Se importa el modelo Persona
from app.Models.PersonaModel import PersonaModel
# Se importa el modelo Ciudad
from app.Models.CiudadModel import CiudadModel
# Se importa el modelo Familia
from app.Models.FamiliaModel import FamiliaModel
# Se importa el modelo ClasificacionSocial
from app.Models.ClasificacionSocialModel import ClasificacionSocialModel
# Se importa el modelo Relacion Familiar
from app.Models.RelacionFamiliarModel import RelacionFamiliarModel
# Se importa el modelo Forma Contacto
from app.Models.FormaContactoModel import FormaContactoModel


# Registrar las rutas en Blueprint
formadmi = Blueprint('registrar_formulario_admision',
                     __name__, template_folder='templates')

# Elaborar las rutas


@formadmi.route('/')
def index_formadmi():

    ad = FormAdmisionModel()
    lista = ad.listar_formularios()

    return render_template('registrar_formulario_admision/index.html', lista=lista)


@formadmi.route('/lista_admision', methods=['GET'])
def lista_admision():
    ad = FormAdmisionModel()
    lista = ad.listar_formularios()

    return jsonify(lista)

# Renderiza el formulario de admision
@formadmi.route('/frm_admi')
def frm_admi():

    lista_personas = datalistPersona()
    lista_padres = datalistPadres()
    lista_ciudades = comboCiudad()
    lista_clasi = comboClasificacionSocial()
    lista_relaciones = comboRelaciones()
    lista_formas = comboFormaContacto()
    lista_familias = comboFamilia()

    return render_template('registrar_formulario_admision/frm_admision.html', lista_personas=lista_personas, lista_padres=lista_padres,
                           lista_ciudades=lista_ciudades, lista_clasi=lista_clasi, lista_relaciones=lista_relaciones,
                           lista_formas=lista_formas, lista_familias=lista_familias)


@formadmi.route('/frm_modificar/<idadmision>')
def frm_modificar(idadmision):

    lista_personas = datalistPersona()
    lista_padres = datalistPadres()
    lista_ciudades = comboCiudad()
    lista_clasi = comboClasificacionSocial()
    lista_relaciones = comboRelaciones()
    lista_formas = comboFormaContacto()
    lista_familias = comboFamilia()

    return render_template('registrar_formulario_admision/frm_modificar.html', lista_personas=lista_personas, lista_padres=lista_padres,
                           lista_ciudades=lista_ciudades, lista_clasi=lista_clasi, lista_relaciones=lista_relaciones,
                           lista_formas=lista_formas, lista_familias =lista_familias)

# Obtener datos del formulario por id via AJAX para modificar.
@formadmi.route('/obtener_formulario_id', methods=['POST'])
def obtener_formulario_id():

    #print(f"Ingresado: {request.json}")
    idadmision = request.json['idadmision']
    ad = FormAdmisionModel()
    datos = ad.obtenerDatosFormularioId(idadmision)

    return jsonify(datos)

@formadmi.route('/obtener_telefonos_id', methods=['POST'])
def obtenerTelefonosId():

    
    idadmision = request.json['idadmision']
    te = FormAdmisionModel()
    data = te.obtenerTelefonos(idadmision)

    return jsonify(data)

@formadmi.route('/obtener_padres_id', methods=['POST'])
def obtenerPadresId():
    
    idadmision = request.json['idadmision']
    te = FormAdmisionModel()
    data = te.obtenerPadres(idadmision)

    return jsonify(data)

# Desde AJAX se procede a guardar.
@formadmi.route('/guardar', methods=['POST'])
def guardar():

    # Obtener datos
    datos = request.json
    
    # Diccionarios
    formulario = datos['formulario']
    lista_padres = datos['arrayPadres'] 
    telefonos = datos['telefonos']

    # Variables
    idpersona = formulario["idpersona"]
    fechanac = formulario["fechanac"]
    direccion = formulario["direccion"]
    idciudad = formulario["idciudad"]
    idsocial = formulario["idsocial"]
    idfamiliar = formulario["idfamilar"]
    fechamatri = formulario["fechamatri"]
    email = formulario["email"]
    postal = formulario["postal"]
    fechaprimercontacto = formulario["fechaprimercontacto"]
    ecivil = formulario["ecivil"]
    sexo = formulario["sexo"]
    formacontacto = formulario["formacontacto"]
    asisteotraigle = formulario["asisteotraigle"]
    requierevisita = formulario["requierevisita"]
    nuevociudad = formulario["nuevociudad"]
    familia = formulario["familia"]
    iglesia = formulario["iglesia"]
    fechaultvisita = formulario["fechaultvisita"]
    idconyuge = formulario["idconyuge"]
    nrohijos = formulario["nrohijos"]

    adm = FormAdmisionModel()
    res = adm.guardar(idpersona, fechanac, direccion, idciudad, idsocial, idfamiliar, fechamatri,
    email, postal, fechaprimercontacto, ecivil, sexo, formacontacto, asisteotraigle, requierevisita, nuevociudad, 
    idconyuge, iglesia, fechaultvisita, nrohijos, familia, lista_padres, telefonos)

    if res == True:
        flash("Exito, se registró correctamente", "success")
        
        return jsonify({"guardado":True})
    else:        
        return jsonify({'guardado': False})

@formadmi.route('/modificar', methods=['POST'])
def modificar():

    #print(f"Ingresado: {request.json}")

    formulario = request.json['formulario']

    idadmision = formulario['idadmision']
    fechanac = formulario['fechanac']
    direccion = formulario['direccion']
    idciudad = formulario['idciudad']
    idsocial = formulario['idsocial']
    idfamiliar =formulario['idfamilar']
    fechamatri = formulario['fechamatri']
    email = formulario['email']
    postal = formulario['postal']
    fechaprimercontacto = formulario['fechaprimercontacto']
    ecivil = formulario['ecivil']
    sexo = formulario['sexo']
    formacontacto = formulario['formacontacto']
    asisteotraigle = formulario['asisteotraigle']
    requierevisita = formulario['requierevisita']
    nuevociudad = formulario['nuevociudad']
    iglesia = formulario['iglesia']
    fechaultvisita = formulario['fechaultvisita']
    idconyuge = formulario['idconyuge']
    nrohijos = formulario['nrohijos']
    familia = formulario['familia']

    borrarTel = request.json['borrarTel']
    agregarTel = request.json['agregarTel']
    nuevosPadres = request.json['nuevosPadres']
    borrarPadres = request.json['borrarPadres']

    ad = FormAdmisionModel()
    res = ad.modificar(idadmision, fechanac.strip(), direccion.strip(), idciudad, idsocial, idfamiliar, fechamatri.strip(), email.strip(), postal.strip(), 
                fechaprimercontacto.strip(), ecivil.strip(), sexo, formacontacto, asisteotraigle, requierevisita, nuevociudad, iglesia.strip(), fechaultvisita.strip(),
                idconyuge, nrohijos.strip(), familia, borrarTel, agregarTel, nuevosPadres, borrarPadres)
    if res == True:
        flash("Exito, se modificó correctamente", "success")
        return jsonify({'guardado': True})
    else:
        return jsonify({'guardado': False})

@formadmi.route('/dar_de_baja', methods=['POST'])
def darBaja():
    
    idadmision = request.json['idadmision']
    razonbaja = request.json['razonbaja']
    obs = request.json['obs']

    
    ad = FormAdmisionModel()
    res = ad.baja(idadmision,razonbaja, obs)

    if res == True:
        flash("Exito, se dio de baja correctamente", "warning")
        return jsonify({"cambiado":True})
    else: 
        return jsonify({"cambiado":False})

@formadmi.route('/obtener_datos_modal', methods=['POST'])
def obtenerDatosModal():

    idadmision = request.json['idadmision']
    
    ad = FormAdmisionModel()

    res = ad.obtenerDatosModal(idadmision)

    return jsonify({'encontrado': res})        

@formadmi.route('/buscar_padre_ajax', methods=["POST"])
def buscarPadres():

    # print(f"request: {request.json}")

    # Se recibe el json como diccionario, se limpia de espacios laterales
    persona = request.json['palabra'].strip()

    # Convertimos el diccionario en una lista, separada por comas
    lista = persona.split(',')

    # Asignamos los valores de la lista
    nombre = lista[0].strip()
    apellido = lista[1].strip()


    # print(f"nombre: {nombre},  apellido: {apellido}")
    pm = PersonaModel()
    # pm.verificarPersona2(nombre, apellido)
    res = PersonaModel.verificarPersona(nombres=nombre, apellidos=apellido)

    return jsonify(dict(existe=res))
    # if res:

    #    return jsonify({"existe": True})

    # else:

    #    return jsonify({"existe": False})


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
        combo += "<option value='" + \
            str(x[0]) + "'>Id:" + str(x[0]) + " - " + \
            str(x[2]) + " " + str(x[3]) + "</option>"
    return combo


def datalistPadres():
    """Funcion datalistPadres.

    Busca en el modelo todas las personas, convierte los resultados
    a cadena, en formato del componente html datalist.

    """
    # Se procesan datos para el datalist
    pm = PersonaModel()
    lista = pm.recuperaPadres()
    combo = ""
    for x in lista:
        combo += "<option value='" + str(x[2]) + ", " + str(x[3]) + "'>"
    return combo


def comboCiudad():
    cm = CiudadModel()
    lista = cm.listarTodos()
    combo = ""
    for ciudad in lista:
        combo += "<option value='" + \
            str(ciudad[0]) + "'>" + str(ciudad[1]) + "</option>\n"
    return combo


def comboClasificacionSocial():
    clsm = ClasificacionSocialModel()
    lista = clsm.obtenerClasificaciones()
    combo = ""
    for item in lista:
        combo += "<option value='" + \
            str(item[0]) + "'>" + str(item[1]) + "</option>\n"
    return combo


def comboRelaciones():
    rfm = RelacionFamiliarModel()
    lista = rfm.obtenerRelaciones()
    combo = ""
    for item in lista:
        combo += "<option value='" + \
            str(item[0]) + "'>" + str(item[1]) + "</option>\n"
    return combo


def comboFormaContacto():
    focm = FormaContactoModel()
    lista = focm.obtenerFormas()
    combo = ""
    for item in lista:
        combo += "<option value='" + \
            str(item[0]) + "'>" + str(item[1]) + "</option>\n"
    return combo

def comboFamilia():
    fam = FamiliaModel()
    lista = fam.listarTodos()
    combo = ""
    for item in lista:
        combo += "<option value='" + \
            str(item[0]) + "'>" + str(item[1]) + "</option>\n"
    return combo
