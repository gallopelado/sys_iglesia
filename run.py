from app import app
from flask import render_template

#app.jinja_env.cache = None
# 'Se consulta si este archivo es el principal, aquel que inicia el sistema.'
if __name__ == "__main__":    
    app.run(debug = True)