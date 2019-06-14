from app import app


#app.jinja_env.cache = None


# En caso de que el usuario quiere manipular url no valida
@app.errorhandler(404)
def handle_bad_request(e):
    return 'Epa!..bad request!', 400


# 'Se consulta si este archivo es el principal, aquel que inicia el sistema.'
if __name__ == "__main__":    
    app.run(debug = True)