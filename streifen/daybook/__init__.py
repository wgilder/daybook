import os
import json
from urllib.request import urlopen

ENV_DEFAULTS = {
    'message': 'Default MotD',
    'api_protocol': 'http',
    'api_port': '9000',
    'api_url': 'localhost',
    'ui_bn': '-1',
    'deploy_env': 'unknown'
}

def env(key, default):
    if (key in os.environ):
        return os.environ[key]
    else:
        return default

DAYBOOK_ENV = {
    'message': env('DAYBOOK_ENV_SPECIFIC_MESSAGE', ENV_DEFAULTS['message']),
    'api_protocol': env('DAYBOOK_API_PROTOCOL', ENV_DEFAULTS['api_protocol']),
    'api_url': env('DAYBOOK_API_URL', ENV_DEFAULTS['api_url']),
    'api_port': env('DAYBOOK_API_PORT', ENV_DEFAULTS['api_port']),
    'ui_bn': env('DAYBOOK_BUILD', ENV_DEFAULTS['ui_bn']),
    'deploy_env': env('DAYBOOK_ENV', ENV_DEFAULTS['deploy_env'])
}

def load_api(name):
    url = DAYBOOK_ENV['api_protocol'] + "://" + DAYBOOK_ENV['api_url'] + ":" + DAYBOOK_ENV['api_port'] + "/v1/" + name
    print (url)
    raw = urlopen(url)
    text = raw.read()
    json_body = json.loads(text.decode('utf-8'))
    return json_body

class Item:
    def __init__(self, name, date, location, amount, currency, description = ""):
        self.name = name
        self.date = date
        self.location = location
        self.amount = amount
        self.currency = currency
        self.description = description

items = [
    Item("Taxi", "May 26", "Waterloo", "25.00", "$", "Train station -> customer"),
    Item("Lunch", "May 27", "Paris", "6.00", "$"),
    Item("Train", "May 30", "Moscow", "27.00", "$", "Return to hotel"),
    Item("Taxi", "June 3", "Honolulu", "8.50", "$", "Train station -> hotel")
]
