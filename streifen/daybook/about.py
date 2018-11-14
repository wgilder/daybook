import json
from streifen.daybook.base import Base
from streifen.daybook import load_api, get_env_value

############################
## About page information ##
############################

class About(Base):
    def __init__(self):
        super().__init__("about.html", "About")
        self._payload = load_api("version")
        self._motd = "Continuous Delivery woot woot!"

    def message(self):
        return self._payload['message']

    def motd(self):
        return self._motd

    def ui_version(self):
        return get_env_value('version')

    def ui_build_number(self):
        return get_env_value('ui_bn')

    def api_version(self):
        return self._payload['version']

    def api_build_number(self):
        return self._payload['buildNumber']

    def author(self):
        return self._payload['author']

    def email(self):
        return self._payload['email']

    def link(self):
        return "index"

    def attributes(self):
        d = super().attributes()
    
        d["message"] = self.message()
        d["motd"] = self.motd()
        d["ui_version"] = self.ui_version()
        d["ui_build_number"] = self.ui_build_number()
        d["api_version"] = self.api_version()
        d["api_build_number"] = self.api_build_number()
        d["author"] = self.author()
        d["email"] = self.email()

        return d