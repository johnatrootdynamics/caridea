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
    username = StringField('username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('password',
                             id='pwd_create',
                             validators=[DataRequired()])
    phone = StringField('phone',
                      id='phone_create',
                      validators=[DataRequired()])
    ad_street = StringField('street',
                      id='street_create',
                      validators=[DataRequired()])
    ad_city = StringField('city',
                      id='city_create',
                      validators=[DataRequired()])
    ad_zip = StringField('zip',
                      id='zip_create',
                      validators=[DataRequired()])
    ad_state = StringField('state',
                      id='state_create',
                      validators=[DataRequired()])
    ad_country = StringField('country',
                      id='country_create',
                      validators=[DataRequired()])
    birthday = StringField('birthday',
                      id='dob_create',
                      validators=[DataRequired()])