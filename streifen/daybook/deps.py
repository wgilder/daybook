import json
from streifen.daybook import load_api, DAYBOOK_ENV

class DependenciesInfo(object):
    def __init__(self):
        env_name = DAYBOOK_ENV['deploy_env'].split('_')[1]
        f = open("/shared-folder/" + env_name + "/info.txt")
        self.info = f.read()
        f.close()

        f = open("/shared-folder/" + env_name + "/build-no.txt")
        self.build_no = f.read()
        f.close()

    def header(self):
        return "Daybook: Dependencies"

    def title(self):
        return "Daybook: Dependencies"

    def deps_build_no(self):
        return self.build_no

    def deps_info(self):
        return self.info

    def deploy_env(self):
        return DAYBOOK_ENV['deploy_env']