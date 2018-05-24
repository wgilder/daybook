# -*- coding: iso-8859-15 -*-
import os

DAYBOOK_ENV = {
    'message': os.environ['DAYBOOK_ENV_SPECIFIC_MESSAGE'],
    'api_port': os.environ['DAYBOOK_API_PORT'],
    'api_url': os.environ['DAYBOOK_API_URL']
}


class Item:
    def __init__(self, name, date, location, amount, currency, description = ""):
        self.name = name
        self.date = date
        self.location = location
        self.amount = amount
        self.currency = currency
        self.description = description

items = [
    Item("Taxi", "May 3", "London", "25.00", "£", "Train station -> customer"),
    Item("Lunch", "May 3", "London", "6.00", "£"),
    Item("Train", "May 3", "London", "27.00", "£", "Return to home"),
    Item("Taxi", "May 3", "London", "8.50", "£", "Train station -> home")
]
