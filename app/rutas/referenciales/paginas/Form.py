from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, SelectField, StringField
from wtforms.validators import DataRequired, length
from app.Models.referenciales.paginas.Pagina_dao import Pagina_dao

class Formulario(FlaskForm):
    obj = Pagina_dao()
    lista = obj.getModulos()

    id = HiddenField()
    campo_pagina = StringField('Nombre Pagina', validators=[DataRequired(), length(max=60)])
    campo_uri = StringField('URI/Modulo/Paquete', validators=[DataRequired(), length(max=60)])
    modulos = SelectField('Elegir Modulo', validators=[], choices=[(item['id'], item["descripcion"]) for item in lista], coerce=int)
    guardar = SubmitField('Guardar')

    # Constructor
    def __init__(self, *args, **kwargs):
        super(Formulario, self).__init__(*args, **kwargs)
        self.modulos.choices = [(item['id'], item["descripcion"]) for item in self.lista]