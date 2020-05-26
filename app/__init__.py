import os
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template
from app.Models.PostulacionModel import PostulacionModel

# Se importan las rutas de recursos.
from app.rutas_recursos.listado_rutas import *

# Trabajando con Schedule
# https://apscheduler.readthedocs.io/en/latest/modules/triggers/interval.html#module-apscheduler.triggers.interval
# Generamos la instancia del modelo.
pos = PostulacionModel()
# Ejecutamos el método al iniciar el sistema.
pos.verificaVencimiento()
# Generamos una instancia para segundo plano con hilos independientes.
sched = BackgroundScheduler(daemon = True)
# Agregamos la tarea para que se espere 1 día para ejecutarse.
sched.add_job( pos.verificaVencimiento, 'interval', days = 1 )
# Iniciar planificador.
sched.start()

# Se inicia una instancia de Flask
app = Flask(__name__)
# En caso de error 404
# En caso de que el usuario quiere manipular url no valida
@app.errorhandler(404)
def handle_bad_request(e):
    #return 'Epa!..bad request!. No existe esta ruta churro.', 400
    return render_template('errores/error404/templates/error404/index.html'), 404

# Definimos rutas estaticas.
app.config['FORM_ADICIONAL_IMAGENES'] = RUTA_IMAGENES_FORM_ADICIONALES
app.config['FORM_DOCUMENTOS_ARCHIVOS'] = RUTA_ARCHIVOS_FORM_DOCUMENTOS
app.config['DOCUMENTOS_POSTULACION'] = RUTA_ARCHIVOS_POSTULACION

# Suponiendo que el error sea el no haber añadido este paquete.
from app import rutas

# Se cargan los modulos de las rutas
from app.rutas.inicio.routes import mod

# Modulos de mantenimiento y seguridad
from app.rutas.referencial_simple.referencial_simple_routes import refs
from app.rutas.ciudad.routes import mod
from app.rutas.nacionalidad.routes import nac
from app.rutas.persona.persona_routes import permod
from app.rutas.profesion.profesion_routes import profesion
from app.rutas.requisito.requisito_routes import reqi
from app.rutas.contrato.contrato_routes import contr

# modulos de membresia
from app.rutas.registrar_formulario_admision.formulario_admision_routes import formadmi
from app.rutas.registrar_formulario_adicional.formulario_adicional_routes import formadi
from app.rutas.registrar_documentos_miembro.documentos_miembro_routes import docm
from app.rutas.registrar_requisitos_miembro.formulario_requisitos_routes import miereq
from app.rutas.registrar_miembro_oficial.miembro_oficial_routes import mieofi
from app.rutas.registrar_formulario_perfil.miembro_perfil_routes import perfil
from app.rutas.registrar_postulacion.postulacion_routes import postu
from app.rutas.registrar_candidatos.registrar_candidatos_routes import candi
from app.rutas.registrar_calificados.registrar_calificados_routes import cali
from app.rutas.registrar_comite.registrar_comite_routes import comi
from app.rutas.registrar_obrero.registrar_obrero_routes import ob

# Modulos de actividades
from app.rutas.gestionar_actividades.registrar_actividades_anuales.actividades_anuales_routes import acan
from app.rutas.gestionar_actividades.registrar_asistencia.registrar_asistencia_routes import asis
from app.rutas.gestionar_actividades.registrar_reserva.reserva_routes import res
from app.rutas.gestionar_actividades.generar_contrato_reserva.generar_contrato_reserva_routes import gcr
from app.rutas.gestionar_actividades.solicitud_hospital.solicitud_hospital_routes import soh
from app.rutas.gestionar_actividades.consejeria.consejeria_routes import cmi

# Modulos de cursos
from app.rutas.gestionar_cursos.malla_curricular.malla_curricular_routes import mc
from app.rutas.gestionar_cursos.planificacion_cursos.planificacion_cursos_routes import pcr
from app.rutas.gestionar_cursos.inscripcion_alumnos.inscripcion_alumnos_routes import insa

# modulos de informes
# Instancia de informes para Mantenimiento y Seguridad
from app.rutas.gestionar_informes.mantenimiento_seguridad.mantenimiento_seguridad_routes import ms
# Instancia de informes para Membresía
from app.rutas.gestionar_informes.membresia.membresia_routes import minf
# Instancia de informes para Actividades
# Instancia de informes para Cursos

# Ordena el espaciado en la plantilla HTML
app.jinja_env.trim_blocks = True

# Se registra las rutas con Blueprints
app.register_blueprint(rutas.inicio.routes.mod)
# Rutas del modulo mantenimiento y seguridad
app.register_blueprint(refs, url_prefix="/referencial_simple")
app.register_blueprint(rutas.ciudad.routes.mod, url_prefix="/ciudad")
app.register_blueprint(rutas.nacionalidad.routes.nac, url_prefix="/nacionalidad")
app.register_blueprint(rutas.persona.persona_routes.permod, url_prefix="/persona")
app.register_blueprint(rutas.profesion.profesion_routes.profesion, url_prefix="/profesion")
app.register_blueprint(rutas.requisito.requisito_routes.reqi, url_prefix='/requisito')
app.register_blueprint(contr, url_prefix='/contrato')

# Rutas del modulo membresia
app.register_blueprint(rutas.registrar_formulario_admision.formulario_admision_routes.formadmi, url_prefix="/formulario_admision")
app.register_blueprint(rutas.registrar_formulario_adicional.formulario_adicional_routes.formadi, url_prefix="/formulario_adicional")
app.register_blueprint(rutas.registrar_documentos_miembro.documentos_miembro_routes.docm, url_prefix="/documentos_miembro")
app.register_blueprint(rutas.registrar_requisitos_miembro.formulario_requisitos_routes.miereq, url_prefix="/requisitos_miembro")
app.register_blueprint(rutas.registrar_miembro_oficial.miembro_oficial_routes.mieofi, url_prefix='/miembro_oficial')
app.register_blueprint(rutas.registrar_formulario_perfil.miembro_perfil_routes.perfil, url_prefix='/membresia/formulario_perfil')
app.register_blueprint(rutas.registrar_postulacion.postulacion_routes.postu, url_prefix='/membresia/formulario_postulacion')
app.register_blueprint(rutas.registrar_candidatos.registrar_candidatos_routes.candi, url_prefix='/membresia/registrar_candidatos')
app.register_blueprint(rutas.registrar_calificados.registrar_calificados_routes.cali, url_prefix='/membresia/registrar_calificados')
app.register_blueprint(rutas.registrar_comite.registrar_comite_routes.comi, url_prefix='/membresia/registrar_comite')
app.register_blueprint(ob, url_prefix='/membresia/registrar_obrero')

# Rutas del modulo actividades
modulo2 = '/actividades'
app.register_blueprint(acan, url_prefix=f'{modulo2}/registrar_actividades_anuales')
app.register_blueprint(asis, url_prefix=f'{modulo2}/registrar_asistencia')
app.register_blueprint(res, url_prefix=f'{modulo2}/registrar_reserva')
app.register_blueprint(gcr, url_prefix=f'{modulo2}/generar_contrato')
app.register_blueprint(soh, url_prefix=f'{modulo2}/solicitud_hospital')
app.register_blueprint(cmi, url_prefix=f'{modulo2}/consejeria')

# Rutas del modulo cursos
modulo3 = '/cursos'
app.register_blueprint(mc, url_prefix=f'{modulo3}/malla_curricular')
app.register_blueprint(pcr, url_prefix=f'{modulo3}/planificacion_cursos')
app.register_blueprint(insa, url_prefix=f'{modulo3}/inscripcion_alumnos')

# Rutas de informes
app.register_blueprint(ms, url_prefix='/informes/mantenimiento_seguridad')
app.register_blueprint(minf, url_prefix='/informes/membresia')

# Codigo secreto para generar la cookie.
#app.secret_key = "12345"
app.secret_key = os.urandom(16)

