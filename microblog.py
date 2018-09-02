"""
Created by Baobaobao123
Thank you 
"""
from app.models import User, Post

__author__ = 'Baobaobao123'

from app import app, db


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run()
