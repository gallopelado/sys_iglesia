from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length

class FormListaReserva(FlaskForm):
    estado = SelectField('Elegir estado:', choices=[('CUALQUIER','CUALQUIER'),('CONFIRMADO', 'CONFIRMADO'), ('NO-CONFIRMADO','NO-CONFIRMADO'),('CANCELADO','CANCELADO'),('DESACTIVADO','DESACTIVADO')])
    fechadesde = DateField('Fecha desde', format='%Y-%m-%d')
    fechahasta = DateField('Fecha hasta', format='%Y-%m-%d')