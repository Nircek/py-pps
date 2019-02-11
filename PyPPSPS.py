#!/usr/bin/env python3
from PPSReply import *

class PyPPSPS:
    def __init__(self, url, server):
        self.url = url
        self.server = server
        self.input = inputfunc
    def connect(self):
        while True:
            self.version = url(self.url+'/pseudophpserver.php')
            if self.version[0] != 'v':
                url.cookie = self.input('Authorization', 'Open ' + self.url+'/cookies.php' + ' and paste here what you get')
            else:
                break
    def log(self, msg):
        perform(self.url, '', {'server':self.server, 'log': msg})
    def pop(self):
        perform(self.url, '', {'server':self.server})
    def reply(self, user, text):
        perform(self.url, '', {'server':self.server, 'text': text, 'user': user})
    def varread(self, user, name):
        perform(self.url, '', {'server':self.server, 'name': name, 'user': user})
    def varwrite(self, user, name, value):
        perform(self.url, '', {'server':self.server, 'name': name, 'user': user, 'value': value})

def main():
    p = PyPPSPS('http://pps.rf.gd', 'test')
    p.connect()
    print(p.version)


if __name__ == '__main__':
    main()
