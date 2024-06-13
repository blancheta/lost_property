from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class LostPropertyForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    phone = StringField('Your Phone Number')
    description = TextAreaField('Description of Lost Item', validators=[DataRequired()])
    photo = FileField('Photo of Lost Item (optional)')
    submit = SubmitField('Submit')
