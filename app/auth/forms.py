"""
Created by Baobaobao123
Thank you 
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User

__author__ = 'Baobaobao123'


class LoginForm(FlaskForm):
    username = StringField(
        _('Username'),
        validators=[DataRequired('请输入用户名')],
        render_kw={
            'placeholder': '请输入用户名'
        })
    password = PasswordField(
        _l('Password'),
        validators=[DataRequired('请输入密码')],
        render_kw={
            'placeholder': '请输入密码'
        }
    )
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))



class RegistrationForm(FlaskForm):
    username = StringField(
        _l('Username'),
        validators=[DataRequired('请输入用户名')],
        render_kw={
            "placeholder": "请输入用户名！",
        }
    )
    email = StringField(
        _l('Email'),
        validators=[DataRequired('请输入邮箱'), Email()],
        render_kw={
            "placeholder": "请输入邮箱！",
        }
    )
    password = PasswordField(
        _l('Password'),
        validators=[DataRequired('请输入密码')],
        render_kw={
            "placeholder": "请输入密码！",
        }
    )
    re_password = PasswordField(
        _l('Repeat Password'),
        validators=[DataRequired('请确认密码'), EqualTo('password', message='两次密码必须相同')],
        render_kw={
            "placeholder": "请再输入一次密码！",
        }
    )
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError(_('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))



class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    re_password = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))
