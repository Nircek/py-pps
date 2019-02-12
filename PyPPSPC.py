#!/usr/bin/env python3
from PPSReply import *
from PPSDefaults import *

class PyPPSPC:
    PPSversion = 'v1.3'
    def __init__(self, url):
        self.url = url
        self.user, self.password = [None]*2
        self.input = inputfunc
        self.bool = boolfunc
    version = lambda self: getVersion(self.url)
    test = lambda self: self.version()[0] == 'v'
    connect = connect
    def register(self, user, password):
        return perform(self.url, 'register', {'user': user, 'pass': password})
    def login(self, user, password):
        self.user = user
        self.password = password
    def push(self, event):
        return perform(self.url, 'push', {'user': self.user, 'pass': self.password, 'event': event})
    def refresh(self):
        return perform(self.url, 'refresh', {'user': self.user, 'pass': self.password})
