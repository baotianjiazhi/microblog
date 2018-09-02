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