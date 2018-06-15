from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo, Email
import re

pattern = r'^[A-Za-z0-9_-]*$'

def latinica_only(form, field):
    if not re.match(pattern, str(field.data)):
        raise ValidationError('Символы могут включать в себя латинские буквы, номера, или - _')


class RegForm(FlaskForm):
    login = StringField(label='Логин', validators=[DataRequired(message='Это обязательное поле.'), latinica_only])
    password = PasswordField(label='Придумайте пароль', validators=[DataRequired(message='Это обязательное поле.'),
                                                                    Length(8, message='Количество символов должно превышать 8.')])
    confirmpass = PasswordField(label='Пароль для подтверждения',
                                validators=[DataRequired(message='Это обязательное поле.'),
                                            Length(8, message='Количество символов должно превышать 8.'),
                                            EqualTo('password', message='Пароли должны совпадать.')])


class LoginForm(FlaskForm):
    login = StringField(label='login', validators=[DataRequired(message='Это обязательное поле.')])
    password = StringField(label='password', validators=[DataRequired(message='Это обязательное поле.')])


class CertForm(FlaskForm):
    file = FileField(label='cert', validators=[DataRequired(message='Это обязательное поле.')])
    submit = SubmitField('Загрузить')
