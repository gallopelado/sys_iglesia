# Se importan las librerías básicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,session,abort

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
@ob.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo'] not in ('ADMIN', 'LIDER'):
        abort(403, description="Acceso prohibido")

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
    ListaObreros = obm.traerObrerosPorComite(idcomite, True) if obm.traerObrerosPorComite(idcomite, True) else None        
    if ListaAdmitidos:
        form.lista_admitido.choices = [ (item[0], str(f'{item[4]} - Fecha {item[2]} - Cantidad Admitidos {item[5]}')) for item in ListaAdmitidos ]
    else:
        form.lista_admitido.choices = [('', 'No hay nueva lista')]    
    return render_template('registrar_obrero/formulario.html', titulo=tituloFormObrero, comite=comite, form=form, lista_admitidos=ListaAdmitidos, lista_obreros=ListaObreros)


@ob.route('/formulario_datos_obrero', methods=['POST'])
def formularioDatosObrero():
    titulo = 'Formulario datos obrero'
    form = FormDatosObrero()
    formGeneral = FormAgregar()
    idcomite = formGeneral.idcomite.data    
    form.idpostulacion.data = formGeneral.lista_admitido.data    
    return render_template('registrar_obrero/formulario_datos_obrero.html', form=form, titulo=titulo , idcomite=idcomite)

@ob.route('/editar_obrero/<int:idcomite>/<int:idobrero>', methods=['GET'])
def mostrarEditarObrero(idcomite, idobrero):    
    titulo = 'Editar datos obrero'
    form = FormDatosObrero()
    lista = obm.traerObrerosPorComiteId(idcomite, idobrero)    
    form.idcomite.data = lista[0]
    form.idobrero.data = lista[1]
    form.obrero.data = lista[2]
    form.fechaingreso.data = lista[3]
    form.entrenamiento.data = True if lista[4]=='SI' else False
    form.observacion.data = lista[5]   
    return render_template('registrar_obrero/formulario_editar_obrero.html', form=form, titulo=titulo, idcomite=idcomite)


@ob.route('/nuevo_obrero', methods=['POST'])
def nuevoObrero():
    obForm = FormDatosObrero()
    if obForm.validate_on_submit():
        next = request.args.get('next', None)
        if next:
            return redirect(next)                    
        # Set datos
        opcion = 'registrar'
        idcomite = obForm.idcomite.data
        idpersona = obForm.idobrero.data
        idpostulacion = obForm.idpostulacion.data
        entrena = obForm.entrenamiento.data
        obs = obForm.observacion.data.strip('')

        # Guardar en el modelo
        res = obm.procesarObrero(opcion, idcomite, idpersona, idpostulacion, entrena, obs, None, None, None)    
        if res == True:
            flash('Se guardó exitosamente el obrero', 'success')
            return redirect(url_for('registrar_obrero.formularioObrero', idcomite=obForm.idcomite.data))
        else:
            flash('Hubo un problema al guardar el obrero, favor contacte con el Administrador del Sistema.', 'danger')
            return redirect(url_for('registrar_obrero.formularioObrero', idcomite=obForm.idcomite.data))        
    print(obForm.errors)
    flash('Hubo un problema al validar el formulario, favor contacte con el Administrador del Sistema.', 'danger')
    return redirect(url_for('registrar_obrero.formularioObrero', idcomite=obForm.idcomite.data))


@ob.route('/baja_obrero', methods=['PUT'])
def bajaObrero():
    idcomite = request.json['idcomite']
    idobrero = request.json['idobrero']
    motivobaja = request.json['observacion']
    ListaAdmitidos = obm.traerPostulacionesProcesadasPorMinisterio(idcomite)[0]
    res = obm.procesarObrero('baja', idcomite, idobrero, ListaAdmitidos[0], None, None, motivobaja, None, None)
    if res == True:
        flash('Se dió de baja un registro', 'success')
        return jsonify({'estado':True, 'mensaje':'Se dio de baja con exito'})
    else:
        flash('Hubo un problema al intentar dar de baja', 'danger')
        return jsonify({'estado':False, 'error':res})

@ob.route('/obrero_dados_de_baja/<int:idcomite>/<string:estado>')
def obrerosDadosDeBaja(idcomite, estado):
    if estado == 'False':
        estado = False
        lista = obm.traerObrerosPorComite(idcomite, estado)
        print(lista)
        return render_template('registrar_obrero/obreros_baja.html', lista=lista)
    else:
        flash('Error al traer datos', 'warning')
        return render_template('registrar_obrero/obreros_baja.html')


@ob.route('/reincorporar_obrero', methods=['PUT'])
def reincorporarObrero():
    idcomite = request.json['idcomite']
    idobrero = request.json['idobrero']
    motivo = request.json['motivo']
    ListaAdmitidos = obm.traerPostulacionesProcesadasPorMinisterio(idcomite)[0]
    res = obm.procesarObrero('reincorporar', idcomite, idobrero, ListaAdmitidos[0], None, None, None, motivo, None)
    if res == True:
        flash('Se reincorporo el registro', 'success')
        return jsonify({'estado':True, 'mensaje':'Se reincorporo el registro con exito'})
    else:
        flash('Hubo un problema al reincorporar', 'danger')
        return jsonify({'estado':False, 'error':res})


# Rutas para ajax
@ob.route('/traer_calificados/<int:idpostulacion>', methods=['GET'])
def traerCalificados(idpostulacion):
    return jsonify(obm.traerCalificadosPorPostulacion(idpostulacion))


@ob.route('/modificar_obrero', methods=['POST'])
def modificarObrero():
    form = FormDatosObrero()        
    opcion = 'modificar'
    idcomite = form.idcomite.data
    ListaAdmitidos = obm.traerPostulacionesProcesadasPorMinisterio(idcomite)[0]
    idpersona = form.idobrero.data
    idpostulacion = ListaAdmitidos[0]
    entrena = form.entrenamiento.data
    obs = form.observacion.data    
    res = obm.procesarObrero(opcion, idcomite, idpersona, idpostulacion, entrena, obs, None, None, None)
    if res == True:
        flash('Se modificó exitosamente el obrero', 'success')
        return redirect(url_for('registrar_obrero.formularioObrero', idcomite=idcomite))
    else:
        flash('Hubo un problema al modificar el obrero, favor contacte con el Administrador del Sistema.', 'danger')
        return redirect(url_for('registrar_obrero.formularioObrero', idcomite=idcomite))