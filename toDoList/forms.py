from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Form_task(FlaskForm):
    description = StringField('Digite sua tarefa:', validators=[DataRequired()])
    button_create = SubmitField('Adicionar')
    button_update = SubmitField('Atualizar')
    button_delete = SubmitField('Deletar')