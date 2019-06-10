from flask import Flask

# Se inicia una instancia de Flask
app = Flask(__name__)

# Se cargan los modulos de las rutas
from app.rutas.inicio.routes import mod
# Modulos de mantenimiento y seguridad
from app.rutas.ciudad.routes import mod
from app.rutas.nacionalidad.routes import mod
from app.rutas.persona.persona_routes import permod
# modulos de membresia
from app.rutas.registrar_formulario_admision.formulario_admision_routes import formadmi

# Ordena el espaciado en la plantilla HTML
app.jinja_env.trim_blocks = True

# Se registra las rutas con Blueprints
app.register_blueprint(rutas.inicio.routes.mod)
# Rutas del modulo mantenimiento y seguridad
app.register_blueprint(rutas.ciudad.routes.mod, url_prefix="/ciudad")
app.register_blueprint(rutas.nacionalidad.routes.mod, url_prefix="/nacionalidad")
app.register_blueprint(rutas.persona.persona_routes.permod, url_prefix="/persona")
# Rutas del modulo membresia
app.register_blueprint(rutas.registrar_formulario_admision.formulario_admision_routes.formadmi, url_prefix="/formulario_admision")



# Codigo secreto para generar la cookie.
app.secret_key = "12345"