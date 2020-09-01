from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length, Email, NumberRange

class RegisterForm(FlaskForm):
    first = TextField(
        'First Name', validators=[DataRequired(), Length(min=1, max=25)]
    )
    last = TextField(
        'Last Name', validators=[DataRequired(), Length(min=1, max=25)]
    )
    username = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Email(message = "not a valid email address"), Length(min=6, max=40)]
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



class SearchForm(Form):
    cuisine = TextField('Cuisine or Restaurant Name')
    time = DateTimeField('Pickup Time')
    submit = SubmitField('Search')
    
    
class RestaurantRegister(Form):
    restaurant = TextField('Restaurant Name', [DataRequired()])
    streetAddress = TextField('Street Address', validators=[DataRequired()])
    city = TextField('City', validators=[DataRequired()])
    state = TextField('State', validators= [DataRequired()])
    zipcode = TextField('Zip Code', validators= [DataRequired()])
    username = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(),Email(message = "not a valid email address"), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        validators= [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )
    
    
class RestaurantLogin(Form):
    username = TextField('Username', validators= [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    
class RestaurantOrders(Form):
    location = TextField('Drop Off Location', validators=[DataRequired()])
    time = DateTimeField('Drop Off Time', validators=[DataRequired()])
    maxOrders = IntegerField('Max Orders', validators=[DataRequired(), NumberRange(min = 0, message = "Must allow at least 1 order!")])