# Importar el modelo Nacionalidad
from app.Models.NacionalidadModel import NacionalidadModel

# Importar el modelo Sangre
from app.Models.SangreModel import SangreModel

# Importar el modelo Profesion.
from app.Models.ProfesionModel import ProfesionModel

# Funciones auxiliares
# 
def listaNacionalidades():
    """Funcion listaNacionalidad.

    Crea instancia del modelo y retorna lista.

    """
    nac = NacionalidadModel()

    return nac.listarTodos()    

def listaSangre():
    """Funcion listaSangre.
    
    Crea instancia del modelo y retorna lista.

    """
    san = SangreModel()

    return san.listarTodos()

def listaProfesion():
    """Funcion listaProfesion.
    
    Crea instancia del modelo y retorna lista.

    """
    prof = ProfesionModel()

    return prof.listarTodos()  