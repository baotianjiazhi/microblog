"""
Created by Baobaobao123
Thank you 
"""
__author__ = 'Baobaobao123'

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes