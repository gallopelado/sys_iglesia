from flask import Blueprint, render_template, redirect, app, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app.rutas.login.FormLogin import FormLogin

#Importar el modelo
from app.Models.seguridad.login.Login_dao import Login_dao

log = Blueprint('login', __name__, template_folder='templates')

@log.route('/login', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if request.method == 'GET':
        return render_template('login/login.html', form=form)
    else:
        isValid = form.validate_on_submit()
        if isValid:
            
            user = form.user.data.strip()
            #password = generate_password_hash(form.loginPassword.data, method='sha256')
            password = form.loginPassword.data
            lg = Login_dao()
            usuarios = lg.searchByUser(user)
            next = request.args.get('next', None)
            if next:
                return redirect(next)

            # Validar la coincidencia o match con el user
            if usuarios and check_password_hash(usuarios['usu_clave'], password):
                # La cosa estuvo buena pancholos, entonces, vamos a poner el estado en linea
                lg.updateStatusUser(True, usuarios['usu_id'])
                # Por supuesto, registramos en el log de usuario
                navegador = f'{request.user_agent.browser}, {request.user_agent.version}'
                ip = request.remote_addr
                obj = {}
                obj['sdlu_nick'] = user
                obj['sdlu_clave'] = usuarios['usu_clave']
                obj['sdlu_latitud'] = None
                obj['sdlu_longitud'] = None
                obj['sdlu_navegador'] = navegador
                obj['sdlu_ip'] = ip
                obj['sdlu_macaddress'] = None
                obj['sdlu_fin_sesion'] = None
                obj['sdlu_estado'] = 'LOGIN'
                obj['creacion_usuario'] = usuarios['usu_id']
                lg.registerLogUser(obj)
                
                # Obtener datos del menu
                menu = lg.getMenuData(usuarios['usu_id'], usuarios['gru_id'])
                
                # Ciertos datos en la sesion
                session['usu_id'] = usuarios['usu_id']
                session['username'] = user.strip()
                session['fechahoy'] = usuarios['fechahoy']
                if menu:
                    session['menu'] = menu
                return redirect(url_for('inicio.index'))
            else:
                # Cuando falla
                bandera = False
                if usuarios and usuarios['usu_nick'].strip() == user.strip():
                    # Si el usuario existe pero no atina la clave, agregar intentos erroneos
                    bandera = True
                    lg = Login_dao()
                    se_data = lg.getSessionData(1)
                    if usuarios['usu_nro_intentos'] < se_data['ses_nro_intentos']:
                        bandera = True
                        #Sumar el intento erroneo
                        lg.updateIntentosErroneosUser(usuarios['usu_id'])
                    else:
                        # Se pone fea la cosa, se supera el limite aceptable por este user, lo bloqueamos por puerco.
                        bandera = True
                        flash('Usuario bloqueado', 'danger')
                        lg.banUser(usuarios['usu_id'], False)
                if bandera:        
                    navegador = f'{request.user_agent.browser}, {request.user_agent.version}'
                    ip = request.remote_addr
                    obj = {}
                    obj['sdlu_nick'] = user
                    obj['sdlu_clave'] = None
                    obj['sdlu_latitud'] = None
                    obj['sdlu_longitud'] = None
                    obj['sdlu_navegador'] = navegador
                    obj['sdlu_ip'] = ip
                    obj['sdlu_macaddress'] = None
                    obj['sdlu_fin_sesion'] = None
                    obj['sdlu_estado'] = 'FAILED'
                    obj['creacion_usuario'] = None
                    lg.registerLogUser(obj)
                flash('Error al loguearse', 'danger')
                return redirect(url_for('login.login'))

        else:
            flash('Error al verificar la sesion', 'danger')
            return redirect(url_for('login.login'))

@log.route('/logout')
def logout():
    if 'username' in session:
        lg = Login_dao()
        # Cambiar status del usuario
        lg.updateStatusUser(False, session['usu_id'])
        # Registrar el log out
        navegador = f'{request.user_agent.browser}, {request.user_agent.version}'
        ip = request.remote_addr
        obj = {}
        obj['sdlu_nick'] = session['username']
        obj['sdlu_clave'] = None
        obj['sdlu_latitud'] = None
        obj['sdlu_longitud'] = None
        obj['sdlu_navegador'] = navegador
        obj['sdlu_ip'] = ip
        obj['sdlu_macaddress'] = None
        obj['sdlu_fin_sesion'] = datetime.now()
        obj['sdlu_estado'] = 'LOGOUT'
        obj['creacion_usuario'] = session['usu_id']
        lg.registerLogUser(obj)
    session.pop('username', None)
    session.pop('menu', None)
    return redirect(url_for('login.login'))