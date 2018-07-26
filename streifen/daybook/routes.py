from flask import render_template
from app import app
from streifen.daybook.dashboard import Dashboard
from streifen.daybook.about import About

def _render(obj):
    attrs = obj.attributes()
    template = obj.template_name()
    return render_template(template, **attrs)

@app.route('/')
@app.route('/index')
def dashboard():
    obj = Dashboard()
    return _render(obj)

@app.route('/about')
def about():
    obj = About()
    return _render(obj)
