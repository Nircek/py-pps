#!/usr/bin/env python3
from PPSReply import *

class PyPPSPC:
    PPSversion = 'v1.3'
    def __init__(self, url):
        self.url = url
        self.user, self.password = [None]*2
        self.input = inputfunc
        self.bool = boolfunc
    def version(self):
        return url(self.url+'/pseudophpserver.php').rstrip('\r\n')
    test = lambda self: self.version()[0] == 'v'
    def connect(self):
        while not self.test():
            url.cookie = self.input('Authorization', 'Open ' + self.url+'/cookies.php' + ' and paste here what you get')
        rv = self.version()
        if rv != self.PPSversion:
            if not self.bool('Version mismatch', 'Your version of PPS is \''+self.PPSversion+'\' but version of chosen server\'s PPS is \''
                             +rv+'\'. Do you want to continue connecting to this server?'):
                raise SystemExit('User chose not to continue connecting to the server.')
    def register(self, user, password):
        perform(self.url, 'register', {'user': user, 'pass': password})
    def login(self, user, password):
        self.user = user
        self.password = password
    def push(self, event):
        perform(self.url, 'push', {'user': self.user, 'pass': self.password, 'event': event})
    def refresh(self):
        perform(self.url, 'refresh', {'user': self.user, 'pass': self.password})

def main():
    p = PyPPSPC('http://pps.rf.gd')
    p.connect()
    print(p.version())
    p.login('root', 'toor')
    p.push('Hello from Python!')

if __name__ == '__main__':
    main()
