"""
Created by Baobaobao123
Thank you 
"""
import datetime
import jwt
import json
from time import time
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from app import db

__author__ = 'Baobaobao123'

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


# 用户模型
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship("Post", backref='author', lazy="dynamic")
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.datetime.now())
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    message_sent = db.relationship('Message',
                                   foreign_keys='Message.sender_id',
                                   backref='author', lazy='dynamic')
    message_received = db.relationship('Message',
                                       foreign_keys='Message.recipient_id',
                                       backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)
    notifications = db.relationship('Notification', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        """设置密码"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """验证密码"""
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        """头像设置"""
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id
        ).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    def new_message(self):
        last_read_time = self.last_message_read_time or datetime.datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time
        ).count()

    def add_notification(self, name, data):
        self.notifications.filter_by(name=name).delete()
        n = Notification(name=name, payload_json=json.dumps(data), user=self)
        db.session.commit()
        return n


class Post(db.Model):
    __tablenname__ = 'post'
    __searchable__ = ['body']
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language = db.Column(db.String(5))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


@login.user_loader
def login_user(id):
    return User.query.get(int(id))


class Message(db.Model):
    __tablenname__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)


class Notification(db.Model):
    __tablenname__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.Float, index=True, default=time)
    payload_json = db.Column(db.Text)

    def get_data(self):
        return json.loads(str(self.payload_json))


class Fiction(db.Model):
    __tablenname__ = 'fiction'
    id = db.Column(db.Integer, primary_key=True)
    fiction_name = db.Column(db.String(128))
    fiction_auth = db.Column(db.String(64))
    fiction_real_url = db.Column(db.String(140))
    fiction_id = db.Column(db.String(100))
    fiction_img = db.Column(db.String(140))
    fiction_comment = db.Column(db.String(140))
    update = db.Column(db.String(400))
    new_content = db.Column(db.String(1024))
    new_url = db.Column(db.String(1024))

    def __repr__(self):
        return '<fiction {}>'.format(self.fiction_name)


class Fiction_List(db.Model):
    __tablename__ = 'fiction_list'
    id = db.Column(db.Integer, primary_key=True)
    fiction_name = db.Column(db.String(255))
    fiction_id = db.Column(db.String(255))
    fiction_lst_url = db.Column(db.String(255))
    fiction_lst_name = db.Column(db.String(255))
    fiction_real_url = db.Column(db.String(255))

    def __repr__(self):
        return '<fiction_list {}>'.format(self.fiction_name)


class Fiction_Content(db.Model):
    __tablename__ = 'fiction_content'
    id = db.Column(db.Integer, primary_key=True)
    fiction_url = db.Column(db.String(255))
    fiction_content = db.Column(db.Text)
    fiction_id = db.Column(db.Integer)
