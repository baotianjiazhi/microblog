"""
Created by Baobaobao123
Thank you 
"""
__author__ = 'Baobaobao123'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '45ecde8ffff745ccb9ce1eb8499bc70e'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:baobaobao123@127.0.0.1:3306/microblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['18271313853@163.com']
    POSTS_PER_PAGE = 25