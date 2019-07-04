from app import app
from flask import render_template

#app.jinja_env.cache = None


# En caso de que el usuario quiere manipular url no valida
@app.errorhandler(404)
def handle_bad_request(e):
    #return 'Epa!..bad request!. No existe esta ruta churro.', 400
    return render_template('errores/error404/templates/error404/index.html')


# 'Se consulta si este archivo es el principal, aquel que inicia el sistema.'
if __name__ == "__main__":    
    app.run(debug = True)