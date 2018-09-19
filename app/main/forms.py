"""
Created by Baobaobao123
Thank you 
"""
from flask_ckeditor import CKEditorField

__author__ = 'Baobaobao123'
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(label=_l('Username'), validators=[DataRequired(message='请输入用户名')])
    about_me = TextAreaField(
        label=_l('About me'),
        validators=[Length(min=0, max=140)]
    )
    submit = SubmitField(label=_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('请使用不同的用户名')


class PostForm(FlaskForm):
    post = CKEditorField(_('Post'))
    submit = SubmitField(_l('Submit'),
                         render_kw={
                             "class": "btn btn-lg btn-success btn-block",
                        },)


class MessageForm(FlaskForm):
    message = CKEditorField(_l('Message'), validators=[
        DataRequired(), Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'), render_kw={
        "style": "float: right;margin-top: 10px",
    })