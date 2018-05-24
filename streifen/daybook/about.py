import json
import urllib2

from streifen.daybook import DAYBOOK_ENV

#json.load(urllib2.urlopen("url"))

class AboutInfo(object):
    def header(self):
        return "Current environment"

    def body(self):
        return DAYBOOK_ENV['message']

    def title(self):
        return "Daybook Information"
