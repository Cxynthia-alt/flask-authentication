from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddUserForm(FlaskForm):
    username = StringField("Username", validators=[
        InputRequired(message="Please fill in your name")])
    password = StringField("Password", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])

    def validate(self, extra_validators=None):
        initial_validation = super(AddUserForm, self).validate()
        if not initial_validation:
            return False
        return True


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[
        InputRequired(message="Please fill in your name")])
    password = StringField("Password", validators=[InputRequired()])

    def validate(self, extra_validators=None):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False
        return True
