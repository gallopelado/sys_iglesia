from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, SelectField, StringField, PasswordField
from wtforms.validators import DataRequired, length
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from app.Models.referenciales.usuarios.Usuario_dao import Usuario_dao

class Formulario(FlaskForm):
    obj = Usuario_dao()
    listaf = obj.getFuncionarios()
    listag = obj.getGrupos()

    id = HiddenField()
    campo_funcionario = StringField('Funcionario')
    nick = StringField('Escriba su nick', validators=[DataRequired(), length(max=6)])
    clave = PasswordField('Escriba su nueva clave', validators=[DataRequired(), length(max=6)])
    funcionario = SelectField('Elegir Funcionario', validators=[DataRequired()],choices=[(item['fun_id'], f'{item["funcionario"]}') for item in listaf], coerce=int)
    grupos = SelectField('Elegir Grupo', choices=[(item['id'], item['descripcion']) for item in listag], coerce=int)
    foto = FileField('Foto')
    guardar = SubmitField('Guardar')

    # Constructor
    def __init__(self, *args, **kwargs):
        super(Formulario, self).__init__(*args, **kwargs)
        self.funcionario.choices = [(item['fun_id'], item["funcionario"]) for item in self.listaf]
        self.grupos.choices = [(item['id'], item['descripcion']) for item in self.listag]