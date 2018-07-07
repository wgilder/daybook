from flask import render_template
from app import app
from streifen.daybook.dashboard import Dashboard
from streifen.daybook.dependencies import Dependencies
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

@app.route('/deps')
def dependencies():
    obj = Dependencies()
    return _render(obj)

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
