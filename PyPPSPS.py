#!/usr/bin/env python3
from .PPSReply import *
from .PPSDefaults import *

class PyPPSPS:
    PPSversion = 'v1.3'
    def __init__(self, url, server):
        self.url = url
        self.server = server
        self.input = inputfunc
        self.bool = boolfunc
    version = lambda self: getVersion(self.url)
    test = lambda self: self.version()[0] == 'v'
    connect = connect
    def log(self, msg):
        return perform(self.url, 'log', {'server':self.server, 'log': msg})
    def pop(self):
        return perform(self.url, 'pop', {'server':self.server})
    def reply(self, user, text):
        return perform(self.url, 'reply', {'server':self.server, 'text': text, 'user': user})
    def varread(self, user, name):
        return perform(self.url, 'varread', {'server':self.server, 'name': name, 'user': user})
    def varwrite(self, user, name, value):
        return perform(self.url, 'varwrite', {'server':self.server, 'name': name, 'user': user, 'value': value})
