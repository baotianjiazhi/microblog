"""
Created by Baobaobao123
Thank you 
"""
__author__ = 'Baobaobao123'

from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
