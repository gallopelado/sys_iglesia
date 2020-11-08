import os

# Se definen las constantes de rutas a utilizarse, para elementos estaticos, como imagenes.

RUTA_MULTIMEDIA = os.path.join(os.path.abspath(os.getcwd()), 'app/static/multimedia/')
RUTA_MEMBRESIA = os.path.join(RUTA_MULTIMEDIA, 'membresia/')
RUTA_USUARIOS = 'static/usuarios'
RUTA_IMAGENES_FORM_ADICIONALES = os.path.join(RUTA_MEMBRESIA, '02_adicionales/imagenes/')
RUTA_ARCHIVOS_FORM_DOCUMENTOS = os.path.join(RUTA_MEMBRESIA, '03_documentos/archivos/')
RUTA_ARCHIVOS_POSTULACION = os.path.join(RUTA_MEMBRESIA, '07_postulacion/documentos/')