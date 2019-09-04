import os
from flask import Flask

# Se importan las rutas de recursos.
from app.rutas_recursos.listado_rutas import *

# Se inicia una instancia de Flask
app = Flask(__name__)

# Definimos rutas estaticas.
app.config['FORM_ADICIONAL_IMAGENES'] = RUTA_IMAGENES_FORM_ADICIONALES
app.config['FORM_DOCUMENTOS_ARCHIVOS'] = RUTA_ARCHIVOS_FORM_DOCUMENTOS

# Suponiendo que el error sea el no haber añadido este paquete.
from app import rutas

# Se cargan los modulos de las rutas
from app.rutas.inicio.routes import mod

# Modulos de mantenimiento y seguridad
from app.rutas.ciudad.routes import mod
from app.rutas.nacionalidad.routes import nac
from app.rutas.persona.persona_routes import permod
from app.rutas.profesion.profesion_routes import profesion
from app.rutas.requisito.requisito_routes import reqi

# modulos de membresia
from app.rutas.registrar_formulario_admision.formulario_admision_routes import formadmi
from app.rutas.registrar_formulario_adicional.formulario_adicional_routes import formadi
from app.rutas.registrar_documentos_miembro.documentos_miembro_routes import docm
from app.rutas.registrar_requisitos_miembro.formulario_requisitos_routes import miereq
from app.rutas.registrar_miembro_oficial.miembro_oficial_routes import mieofi
from app.rutas.registrar_formulario_perfil.miembro_perfil_routes import perfil
from app.rutas.registrar_postulacion.postulacion_routes import postu

# Ordena el espaciado en la plantilla HTML
app.jinja_env.trim_blocks = True

# Se registra las rutas con Blueprints
app.register_blueprint(rutas.inicio.routes.mod)
# Rutas del modulo mantenimiento y seguridad
app.register_blueprint(rutas.ciudad.routes.mod, url_prefix="/ciudad")
app.register_blueprint(rutas.nacionalidad.routes.nac, url_prefix="/nacionalidad")
app.register_blueprint(rutas.persona.persona_routes.permod, url_prefix="/persona")
app.register_blueprint(rutas.profesion.profesion_routes.profesion, url_prefix="/profesion")
app.register_blueprint(rutas.requisito.requisito_routes.reqi, url_prefix='/requisito')

# Rutas del modulo membresia
app.register_blueprint(rutas.registrar_formulario_admision.formulario_admision_routes.formadmi, url_prefix="/formulario_admision")
app.register_blueprint(rutas.registrar_formulario_adicional.formulario_adicional_routes.formadi, url_prefix="/formulario_adicional")
app.register_blueprint(rutas.registrar_documentos_miembro.documentos_miembro_routes.docm, url_prefix="/documentos_miembro")
app.register_blueprint(rutas.registrar_requisitos_miembro.formulario_requisitos_routes.miereq, url_prefix="/requisitos_miembro")
app.register_blueprint(rutas.registrar_miembro_oficial.miembro_oficial_routes.mieofi, url_prefix='/miembro_oficial')
app.register_blueprint(rutas.registrar_formulario_perfil.miembro_perfil_routes.perfil, url_prefix='/membresia/formulario_perfil')
app.register_blueprint(rutas.registrar_postulacion.postulacion_routes.postu, url_prefix='/membresia/formulario_postulacion')

# Codigo secreto para generar la cookie.
app.secret_key = "12345"