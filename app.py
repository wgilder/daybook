from flask import Flask
app = Flask(__name__)
from streifen.daybook import routes
# from authlib.flask.client import OAuth

# oauth = OAuth(app)

# auth0 = oauth.register(
#     'auth0',
#     client_id='3R3giYTTX0FaN4p538HX8rHK7hyXXuhb',
#     client_secret='YOUR_CLIENT_SECRET',
#     api_base_url='https://daybook.eu.auth0.com',
#     access_token_url='https://daybook.eu.auth0.com/oauth/token',
#     authorize_url='https://daybook.eu.auth0.com/authorize',
#     client_kwargs={
#         'scope': 'openid profile',
#     },
# )
