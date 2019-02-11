#!/usr/bin/env python3
from PPSReply import *
from urllib.request import Request, urlopen
def url(uri):
    q = Request(uri)
    q.add_header('User-Agent', 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405')
    q.add_header('Cookie', url.cookie)
    return urlopen(q).read().decode()
url.cookie = '__test=eb93faad212ed7dc5ddc4a144182d12d '

def inputfunc(title, msg):
    print(title, msg, sep='\n')
    return input()

class PyPPSPS:
    def __init__(self, url, server):
        self.url = url
        self.server = server
    def connect(self):
        while True:
            self.version = url(self.url+'/pseudophpserver.php')
            if self.version[0] != 'v':
                url.cookie = inputfunc('Authorization', 'Open ' + self.url+'/cookies.php' + ' and paste here what you get')
            else:
                break
    def log(self, msg):
        pass
    def pop(self):
        pass
    def reply(self, user, text):
        pass
    def varread(self, user, name):
        pass
    def varwrite(self, user, name, value):
        pass

def main():
    p = PyPPSPS('http://pps.rf.gd', 'test')
    p.connect()
    print(p.version)


if __name__ == '__main__':
    main()
