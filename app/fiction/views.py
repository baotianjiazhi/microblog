from flask import render_template

from app import db
from app.models import Fiction
from . import bp as fiction

@fiction.route('/book')
def book_index():
    fictions = Fiction().query.all()
    print(fictions)
    return render_template('fiction/fiction_index.html', fictions=fictions)
