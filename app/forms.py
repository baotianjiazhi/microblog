"""
Created by Baobaobao123
Thank you 
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

from app.models import User

__author__ = 'Baobaobao123'


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired('请输入用户名')],
        render_kw={
            'placeholder': '请输入用户名'
        })
    password = PasswordField(
        'Password',
        validators=[DataRequired('请输入密码')],
        render_kw={
            'placeholder': '请输入密码'
        }
    )
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired('请输入用户名')],
        render_kw={
            "placeholder": "请输入用户名！",
        }
    )
    email = StringField(
        'Email',
        validators=[DataRequired('请输入邮箱'), Email()],
        render_kw={
            "placeholder": "请输入邮箱！",
        }
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired('请输入密码')],
        render_kw={
            "placeholder": "请输入密码！",
        }
    )
    re_password = PasswordField(
        'Rereapt Password',
        validators=[DataRequired('请确认密码'), EqualTo('password', message='两次密码必须相同')],
        render_kw={
            "placeholder": "请再输入一次密码！",
        }
    )
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Please use a different email.')


class EditProfileForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(message='请输入用户名')])
    about_me = TextAreaField(
        label='About me',
        validators=[Length(min=0, max=140)]
    )
    submit = SubmitField(label='Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username')


class PostForm(FlaskForm):
    post = TextAreaField(label='Say something', validators=[
        DataRequired(), Length(min=1, max=140)
    ])
    submit = SubmitField('Submit')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    re_password = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
