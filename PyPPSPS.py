#!/usr/bin/env python3
from .PPSReply import *
from .PPSDefaults import *
import json

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
    def varread(self, user, name=None):
        if name is None:
            name = user
            user = ''
        return perform(self.url, 'varread', {'server':self.server, 'name': name, 'user': user})
    def varwrite(self, user, name, value=None):
        if value is None:
            value = name
            name = user
            user = ''
        return perform(self.url, 'varwrite', {'server':self.server, 'name': name, 'user': user, 'value': value})
    def popj(self):
        o = self.pop()
        r = loads(o[1])
        r['user'] = o[0]
        return r
    def replyj(self, user, text):
        return self.reply(user, json.dumps(text))
    def varreadj(self, user, name=None):
        return loads(joinUS(self.varread(user, name)))
    def varwritej(self, user, name, value=None):
        if value is None:
            return self.varwrite(user, json.dumps(name))
        else:
            return self.varwrite(user, name, json.dumps(value))
