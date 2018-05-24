from flask import Flask
app = Flask(__name__)
from streifen.daybook import routes

