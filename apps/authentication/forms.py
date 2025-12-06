# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])
    phone = StringField('Phone',
                      id='phone_create',
                      validators=[DataRequired()])
    ad_street = StringField('Street',
                      id='street_create',
                      validators=[DataRequired()])
    ad_city = StringField('City',
                      id='city_create',
                      validators=[DataRequired()])
    ad_state = StringField('State',
                      id='state_create',
                      validators=[DataRequired()])
    ad_country = StringField('Country',
                      id='country_create',
                      validators=[DataRequired()])
    birthday = DateField('Birthday',
                      id='dob_create', format='%Y-%m-%d',
                      validators=[DataRequired()])