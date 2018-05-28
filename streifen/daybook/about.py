import json
from streifen.daybook import load_api, DAYBOOK_ENV

class AboutInfo(object):
    def __init__(self):
        self.payload = load_api("version")
        self._motd = "Welcome to Berlin!"

    def header(self):
        return "Daybook: About"

    def title(self):
        return "Daybook: About"

    def message(self):
        return self.payload['message']

    def motd(self):
        return self._motd

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

    def deploy_env(self):
        return DAYBOOK_ENV['deploy_env']
