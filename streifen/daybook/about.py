import json
from streifen.daybook import load_api, DAYBOOK_ENV

motd = "Default MotD"

class AboutInfo(object):
    def __init__(self):
        self.payload = load_api("version")

    def header(self):
        return "Daybook: About"

    def title(self):
        return "Daybook: About"

    def message(self):
        return self.payload['message']

    def ui_version(self):
        return self.payload['version']

    def ui_build_number(self):
        return DAYBOOK_ENV['ui_bn']

    def api_version(self):
        return self.payload['version']

    def api_build_number(self):
        return self.payload['buildNumber']

    def author(self):
        return self.payload['author']

    def email(self):
        return self.payload['email']
