from flask import render_template
from app import app
from streifen.daybook.SayHello import SayHello
from streifen.daybook.Dashboard import Dashboard
from streifen.daybook.about import AboutInfo
import pystache

@app.route('/')
@app.route('/index')
def dashboard():
    db = Dashboard()
    renderer = pystache.Renderer()
    return renderer.render(db)

@app.route('/hello')
def hello():
    hello = SayHello()
    renderer = pystache.Renderer()
    return renderer.render(hello)

@app.route('/about')
def about():
    about = AboutInfo()
    renderer = pystache.Renderer()
    return renderer.render(about)
