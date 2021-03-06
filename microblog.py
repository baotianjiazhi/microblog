"""
Created by Baobaobao123
Thank you 
"""
from app.models import User, Post, Message, Notification

__author__ = 'Baobaobao123'

from app import db, cli, create_app
from flask import current_app

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Messages': Message, 'Notification': Notification}


if __name__ == '__main__':
    app.run()