from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length

class FormListaActividadesAnuales(FlaskForm):
    organizador = SelectField('Elegir organizador:')
    lugar = SelectField('Elegir lugar')
    fechadesde = DateField('Fecha desde', format='%Y-%m-%d')
    fechahasta = DateField('Fecha hasta', format='%Y-%m-%d')