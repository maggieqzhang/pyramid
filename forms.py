from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(FlaskForm):
    first = TextField(
        'First Name', validators=[DataRequired(), Length(min=1, max=25)]
    )
    last = TextField(
        'Last Name', validators=[DataRequired(), Length(min=1, max=25)]
    )
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        validators = [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )
    submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
    username = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Login')


class ForgotForm(FlaskForm):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    submit = SubmitField('Submit')
