from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddUserForm(FlaskForm):
    username = StringField("Username", validators=[
        InputRequired(message="Please fill in your name")])
    password = StringField("Password", validate_choice=[InputRequired()])
    email = StringField("Email", validate_choice=[InputRequired()])
    first_name = StringField("First Name", validate_choice=[InputRequired()])
    last_name = StringField("Last Name", validate_choice=[InputRequired()])
