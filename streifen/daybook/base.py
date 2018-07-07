from streifen.daybook import get_env_value

class Base(object):
    def __init__(self, template_name, title = "Hello", header = None):
      if not template_name: 
          raise ValueError("template name not set")

      self._title = title
      self._header = self._title if header is None else header
      self._template_name = template_name
    
    def attributes(self):
        d = { 
            "deploy_env": self.deploy_env(),
            "title": self._title,
            "header": self._header,
            "footer": self.deploy_env()
        }
        return d

    def deploy_env(self):
        return get_env_value('deploy_env')

    def template_name(self):
        return self._template_name
