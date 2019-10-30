# Se importan las librerías básicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar modelo
from app.Models.ComiteModel import ComiteModel
from app.Models.ObreroModel import ObreroModel

# Importar formularios
from app.rutas.registrar_obrero.formularios import FormAgregar, FormDatosObrero

# Registrar en Blueprint
ob = Blueprint('registrar_obrero', __name__, template_folder='templates')
titulo = 'Registrar Obreros a Comité'
tituloFormObrero = 'Formulario Lista de Obreros'
cm = ComiteModel()
obm = ObreroModel()

# Rutas
@ob.route('/')
def index_obrero():    
    lista = cm.traerTodos()       
    return render_template('registrar_obrero/index.html', titulo=titulo, lista=lista)


@ob.route('/formulario_obrero/<int:idcomite>', methods=['GET'])
def formularioObrero(idcomite):    
    comite = cm.traerPorId(idcomite)
    form = FormAgregar() 
    # Setear formulario
    form.idcomite.data = comite[0]
    form.comite.data = comite[1] 
    form.idlider.data = comite[2]
    form.lider.data = comite[3]    
    ListaAdmitidos = obm.traerPostulacionesProcesadasPorMinisterio(idcomite)
    if ListaAdmitidos:
        form.lista_admitido.choices = [ (item[0], str(f'{item[4]} - Fecha {item[2]} - Cantidad Admitidos {item[5]}')) for item in ListaAdmitidos ]
    else:
        form.lista_admitido.choices = [('', 'No hay nueva lista')]    
    return render_template('registrar_obrero/formulario.html', titulo=tituloFormObrero, comite=comite, form=form, lista_admitidos=ListaAdmitidos)


@ob.route('/formulario_datos_obrero', methods=['POST'])
def formularioDatosObrero():
    titulo = 'Formulario datos obrero'
    form = FormDatosObrero()
    formGeneral = FormAgregar()
    idcomite = formGeneral.idcomite.data    
    form.idpostulacion.data = formGeneral.lista_admitido.data    
    return render_template('registrar_obrero/formulario_datos_obrero.html', form=form, titulo=titulo , idcomite=idcomite)


# Rutas para ajax
@ob.route('/traer_calificados/<int:idpostulacion>', methods=['GET'])
def traerCalificados(idpostulacion):
    return jsonify(obm.traerCalificadosPorPostulacion(idpostulacion))