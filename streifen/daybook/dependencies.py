import json
from streifen.daybook.base import Base
from streifen.daybook import load_api, get_env_value

class Dependencies(Base):
    def __init__(self):
        super().__init__("dependencies.html", "Dependencies")
        env_name = get_env_value('deploy_env').split('_')[1]
        f = open("/shared-folder/" + env_name + "/info.txt")
        self.info = f.read()
        f.close()

        f = open("/shared-folder/" + env_name + "/build-no.txt")
        self.build_no = f.read()
        f.close()

    def deps_build_no(self):
        return self.build_no

    def deps_info(self):
        return self.info

    def attributes(self):
        d = super().attributes()
    
        d["deps_info"] = self.deps_info()
        d["deps_build_no"] = self.deps_build_no()

        return d