"""
Created by Baobaobao123
Thank you 
"""
__author__ = 'Baobaobao123'


from flask import  Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers



