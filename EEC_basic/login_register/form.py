# from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email, ValidationError
from login_register.models import User


class RegisterForm(FlaskForm):
    def validate_email(self, email_to_check):
        em = User.query.filter_by(email=email_to_check.data).first()
        if em:
            raise ValidationError('This email is already registered')

    name = StringField(label='Enter your name:', validators=[DataRequired()])
    email = StringField(label='Enter your email_address', validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Set a Password', validators=[Length(min=4, max=12),DataRequired()])
    password2 = PasswordField(label='Confirm password', validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm):
    email = StringField(label='Enter your email_address', validators=[Email(),DataRequired()])
    password = PasswordField(label='Enter your Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')
