"""
Created by Baobaobao123
Thank you 
"""
__author__ = 'Baobaobao123'

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.flaskenv'))

class Config(object):
    SECRET_KEY = '45ecde8ffff745ccb9ce1eb8499bc70e'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:baobaobao123@127.0.0.1:3306/microblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 是否追踪修改
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['123456@163.com']
    LANGUAGES = ['zh', 'en']
    POSTS_PER_PAGE = 25

