from flask import render_template
from app import app
from streifen.daybook.SayHello import SayHello
from streifen.daybook.Dashboard import Dashboard
from streifen.daybook.deps import DependenciesInfo
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

@app.route('/deps')
def dependencies():
    deps = DependenciesInfo()
    renderer = pystache.Renderer()
    return renderer.render(deps)

@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }

    return redirect('/')

@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri='/', audience='https://daybook.eu.auth0.com/userinfo')
