#!/usr/bin/env python3
from urllib.request import Request, urlopen
def url(url):
  q = Request(url)
  q.add_header('User-Agent', 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405')
  q.add_header('Cookie', '__test=84955b7c4d6c13ba5eeddd6fcde61533')
  return urlopen(q).read().decode()
class PyPPSPS:
    def __init__(self, url, server):
        self.url = url
        self.server = server
    def connect(self):
        pass
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

if __name__ == '__main__':
    print(url('http://pps.rf.gd/pseudophpserver.php'))
