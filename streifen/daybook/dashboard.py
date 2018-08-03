from streifen.daybook.base import Base
from streifen.daybook import items

class Dashboard(Base):
    def __init__(self):
        super().__init__("dashboard.html", "Open Items")

    def body(self):
        return "August 3rd, 2018 ({} item{})".format(len(items), "" if len(items)==1 else "s")

    def items(self):
        return items

    def attributes(self):
        d = super().attributes()
        d["body"] = self.body()
        d["items"] = self.items()

        return d
