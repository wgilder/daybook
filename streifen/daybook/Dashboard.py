from streifen.daybook import items

class Dashboard(object):
    def header(self):
        return "Daybook: Open Items"

    def body(self):
        return "May 29th, 2018 ({} item{})".format(len(items), "" if len(items)==1 else "s")

    def title(self):
        return "Open Items"

    def items(self):
        return items

