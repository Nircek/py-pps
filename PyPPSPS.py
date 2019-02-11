#!/usr/bin/env python3
from urllib.request import Request, urlopen
from enum import Enum
def url(uri):
    q = Request(uri)
    q.add_header('User-Agent', 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405')
    q.add_header('Cookie', url.cookie)
    return urlopen(q).read().decode()
url.cookie = '__test=eb93faad212ed7dc5ddc4a144182d12d '

class PPSCode(Enum):
    GOOD = 0
    ERROR = 1
    DBERROR = 2
    UNEXPECTEDERROR = 3
    def get(s):
        d = {'0': PPSCode.GOOD, '-': PPSCode.ERROR, '+': PPSCode.DBERROR}
        if len(s) == 0 or not s[0] in d:
            return PPSCode.UNEXPECTEDERROR
        else:
            return d[s[0]]

class Reply:
    def __init__(self, s):
        s=s.rstrip('\r\n')
        self.type = PPSCode.get(s)
        if self.type != PPSCode.UNEXPECTEDERROR:
            s = s[1:]
        self.args = s.split('\N{Symbol For Unit Separator}')
    def __repr__(self):
        return 'Reply' + repr((self.type, self.args))

class PyPPSPS:
    def inputfunc(self, title, msg):
        print(title, msg, sep='\n')
        return input()
    def __init__(self, url, server):
        self.url = url
        self.server = server
    def connect(self):
        while True:
            self.version = url(self.url+'/pseudophpserver.php')
            if self.version[0] != 'v':
                url.cookie = self.inputfunc('Authorization', 'Open ' + self.url+'/cookies.php' + ' and paste here what you get')
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
