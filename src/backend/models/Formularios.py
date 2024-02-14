from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    SelectField,
    IntegerField,
    HiddenField,
)
from wtforms.validators import DataRequired, Email, Regexp, Length, EqualTo, NumberRange


class MyForm(FlaskForm):
    AlphaNumerico = r"^[a-zA-Z0-9]+$"
    AlphaNumerico_Caracter = r"^(?=.*[0-9])(?=.*[!@#$%^&*])"
    Name = StringField("Name", validators=[DataRequired()])
    LastName = StringField("LastName", validators=[DataRequired()])
    Email = StringField(
        "Correo",
        validators=[
            DataRequired(),
            Email(message="Ingrese una dirección de correo electrónico válida"),
        ],
    )
    Username = StringField(
        "Usuario",
        validators=[
            DataRequired(),
            Length(min=4, max=30),
            Regexp(
                AlphaNumerico,
                message="Solo se permiten letras y números en el username",
            ),
        ],
    )
    Password = PasswordField(
        "Password",
        validators=[
            Length(min=6, max=20),
            Regexp(
                AlphaNumerico_Caracter,
                message="La contraseña debe contener al menos un número y un carácter especial",
            ),
        ],
    )
    Confirm_Password = PasswordField(
        "Password2",
        validators=[
            DataRequired(),
            EqualTo("Password", message="Las contraseñas deben coincidir"),
        ],
    )
    Submit = SubmitField("Crear")


class HuellaCarbonoForm(FlaskForm):
    Sel_Categoria = SelectField(
        "Sel_Categoria",
        choices=[],
        validators=[DataRequired()],
        render_kw={"style": "display: none"},
    )
    Sel_Fuente = SelectField(
        "Sel_Fuente",
        choices=[],
        validators=[DataRequired()],
        render_kw={"style": "display: none"},
    )
    Sel_Datos = SelectField(
        "Sel_Datos",
        choices=[],
        validators=[DataRequired()],
        coerce=int,
        render_kw={"style": "display: none"},
    )
    input_container = IntegerField("Dato", validators=[NumberRange(min=0)])
    boton_calcular = SubmitField("Calcular")
    csrf_token = HiddenField("CSRF Token")
