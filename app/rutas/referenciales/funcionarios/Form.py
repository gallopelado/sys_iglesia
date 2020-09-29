from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, SelectField, StringField
from wtforms.validators import DataRequired
from app.Models.referenciales.funcionarios.Funcionario_dao import Funcionario_dao

class Formulario(FlaskForm):
    obj = Funcionario_dao()
    listap = obj.getPersonas(1)
    listac = obj.getCargos()

    id = HiddenField()
    campo_persona = StringField('Funcionario')
    personas = SelectField('Elegir Persona', validators=[DataRequired()],choices=[(item['per_id'], f'{item["persona"]}') for item in listap], coerce=int)
    cargos = SelectField('Elegir Cargo', choices=[(item['id'], item['descripcion']) for item in listac], coerce=int)
    guardar = SubmitField('Guardar')

    # Constructor
    def __init__(self, *args, **kwargs):
        super(Formulario, self).__init__(*args, **kwargs)
        self.personas.choices = [(item['per_id'], f'{item["persona"]}') for item in self.listap]
        self.cargos.choices = [(item['id'], item['descripcion']) for item in self.listac]