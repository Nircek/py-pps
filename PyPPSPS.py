#!/usr/bin/env python3
from PPSReply import *

class PyPPSPS:
    PPSversion = 'v1.3'
    def __init__(self, url, server):
        self.url = url
        self.server = server
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

def main():
    p = PyPPSPS('http://pps.rf.gd', 'test')
    p.connect()
    print(p.version())
    print(p.pop())


if __name__ == '__main__':
    main()
