import os
import json
from urllib.request import urlopen

def get_env_value(key, default=None):
    if key in _DAYBOOK_ENVS:
        val = _DAYBOOK_ENVS[key]
        return val if val else default

    return default

def load_api(name):
    url = _DAYBOOK_ENVS['api_protocol'] + "://" + _DAYBOOK_ENVS['api_url'] + ":" + _DAYBOOK_ENVS['api_port'] + "/v1/" + name
    print (url)
    raw = urlopen(url)
    text = raw.read()
    json_body = json.loads(text.decode('utf-8'))
    return json_body
    
def _env(key, default):
    if (key in os.environ):
        return os.environ[key]
    else:
        return default

class Item:
    def __init__(self, name, date, location, amount, currency, description = ""):
        self.name = name
        self.date = date
        self.location = location
        self.amount = amount
        self.currency = currency
        self.description = description

items = [
    Item("Taxi", "July 23", "Waterloo, Iowa", "25.00", "$", "Train station -> customer"),
    Item("Lunch", "July 24", "Paris, Texas", "6.00", "$"),
    Item("Train", "July 26", "Moscow, Idaho", "27.00", "$", "Return to hotel"),
    Item("Taxi", "July 27", "New York, Kentucky", "8.50", "$", "Train station -> hotel")
]

_ENV_DEFAULTS = {
    'message': 'Default MotD',
    'api_protocol': 'http',
    'api_port': '9000',
    'api_url': 'localhost',
    'ui_bn': '-1',
    'deploy_env': 'env_unknown'
}

_DAYBOOK_ENVS = {
    'message': _env('DAYBOOK_ENVS_SPECIFIC_MESSAGE', _ENV_DEFAULTS['message']),
    'api_protocol': _env('DAYBOOK_API_PROTOCOL', _ENV_DEFAULTS['api_protocol']),
    'api_url': _env('DAYBOOK_API_URL', _ENV_DEFAULTS['api_url']),
    'api_port': _env('DAYBOOK_API_PORT', _ENV_DEFAULTS['api_port']),
    'ui_bn': _env('DAYBOOK_BUILD', _ENV_DEFAULTS['ui_bn']),
    'deploy_env': _env('DAYBOOK_ENV', _ENV_DEFAULTS['deploy_env'])
}
