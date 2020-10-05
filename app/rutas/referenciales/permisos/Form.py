from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, SelectField, StringField, BooleanField
from wtforms.validators import DataRequired, length
from app.Models.referenciales.paginas.Pagina_dao import Pagina_dao

class Formulario(FlaskForm):
    obj = Pagina_dao()
    lista = obj.getModulos()

    gru_id = HiddenField()
    pag_id = HiddenField()
    nombre_grupo = StringField('Grupo Seleccionado')
    nombre_pagina = StringField('Nombre de Pagina')
    modulos = SelectField('Elegir Modulo', validators=[], choices=[(item['id'], item["descripcion"]) for item in lista], coerce=int)
    paginas = SelectField('Escoger pagina', choices=[('..', '..')])
    leer = BooleanField('Leer')
    insertar = BooleanField('Insertar')
    editar = BooleanField('Editar')
    borrar = BooleanField('Borrar')

    # Constructor
    def __init__(self, *args, **kwargs):
        super(Formulario, self).__init__(*args, **kwargs)
        self.modulos.choices = [(item['id'], item["descripcion"]) for item in self.lista]