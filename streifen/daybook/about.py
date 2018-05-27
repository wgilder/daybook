import json
from streifen.daybook import load_api

class AboutInfo(object):
    def __init__(self):
        self.payload = load_api("version")

    def header(self):
        return "Daybook: About"

    def title(self):
        return "Daybook App Info"

    def message(self):
        return self.payload['message']

    def version(self):
        return self.payload['version']

    def build_number(self):
        return self.payload['buildNumber']

    def author(self):
        return self.payload['author']

    def email(self):
        return self.payload['email']
