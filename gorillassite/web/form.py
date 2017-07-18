from flask.ext.wtf.form import Form
from flask.ext.wtf.recaptcha.fields import RecaptchaField
from flask.ext.wtf.recaptcha.validators import Recaptcha
from wtforms.fields.core import StringField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email


__author__ = 'abreu'


class Contact(Form):

    name = StringField('Nome', [DataRequired(message="Nome é obrigatório")])

    mail = StringField('Email', [DataRequired(message="Email é obrigatório"), Email(message="Email inválido")])

    phone = StringField('Telefone 41 4063-5035')

    message = TextAreaField('Mensagem', [DataRequired(message="Mensagem é obrigatória")])

    recaptcha = RecaptchaField(validators=[Recaptcha(message="Responda o captcha corretamente")])
