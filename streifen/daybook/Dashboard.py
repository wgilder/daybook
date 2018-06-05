from streifen.daybook import items, DAYBOOK_ENV

class Dashboard(object):
    def header(self):
        return "Daybook: Open Items"

    def body(self):
        return "June 5th, 2018 ({} item{})".format(len(items), "" if len(items)==1 else "s")

    def title(self):
        return "Open Items"

    def items(self):
        return items

    def deploy_env(self):
        return DAYBOOK_ENV['deploy_env']

