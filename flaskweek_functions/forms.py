from wtforms import Form, validators, StringField, PasswordField
from wtforms import SelectField, TextAreaField, BooleanField, DateTimeField, EmailField, HiddenField, IntegerRangeField, RadioField, SubmitField
import email_validator

# creation d'une classe de formulaire pour le login
class UserLogin(Form):
    uid = StringField("Username or E-mail", validators=[validators.InputRequired(), validators.Length(min=4, max=15)])
    pwd = PasswordField("Password", validators=[validators.InputRequired()])#, widget=PasswordInput(hide_value=False))

class loginWTF(Form):
    uid = StringField("Email or username", validators=[validators.InputRequired(), validators.Length(min=5, max=15, message="La longueur doit etre comprise entre 5 et 15 chars")])
    pwd = PasswordField("Password", validators=[validators.InputRequired(), validators.equal_to('pwd2', message='PASSWORDS DONT MATCH')])
    pwd2 = PasswordField("confirm password", validators=[validators.InputRequired()])

class ExampleForms(Form):
    uNom = StringField("Nom", validators=[validators.InputRequired(), validators.Length(min=3)])
    uSexe = SelectField("Sexe", validators=[validators.Optional()], choices=[('H', "Homme"), ('F', "Femme"), ('A', "Autre")])
    uAPropos = TextAreaField("A propos de vous", validators=[validators.Optional()])
    uMdp = PasswordField("Password", validators=[validators.InputRequired(), validators.equal_to('uMdpConfirmation', message='PASSWORDS DONT MATCH')])
    uMdpConfirmation = PasswordField("Confirmer", validators=[validators.InputRequired()])
    uConnecter = BooleanField("Rester connecter ?", default=True)
    uAnniversaire = DateTimeField("Date d'anniversaire", validators=[validators.Optional()], format='%m-%d-%Y')
    uEmail = EmailField("Email", validators=[validators.InputRequired(), validators.Email(), ])
    uHidden = HiddenField("ceci est un input cache")
    uIntegerRange = IntegerRangeField("Input range", [validators.NumberRange(min=0, max=100)])
    uRadio = RadioField('Sexe', choices=[(1,'Homme'), (2,'Femme'), (3,'Autre')])
    btnSubmit = SubmitField("example")