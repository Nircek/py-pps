#!/usr/bin/env python3
from urllib.request import Request, urlopen
from urllib.parse import quote_plus, urlencode
from .PPSReply import *
import warnings

def url(uri, data={}):
    try:
        q = Request(uri)
        q.add_header('User-Agent', 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405')
        q.add_header('Cookie', url.cookie)
        return urlopen(q, data=urlencode(data).encode()).read().decode()
    except Exception:
        print(uri)
        raise
url.cookie = '__test=c3495eae2f165b2aa28f8d430d413014 '

def perform(uri, cmd, params={}):
    return PPSReply(url(uri+'/'+cmd+'.php', params)).exec()

getVersion = lambda uri: url(uri+'/pseudophpserver.php').rstrip('\r\n')
joinUS = lambda x: x[0] if x[1] == '' else '\N{Symbol For Unit Separator}'.join(x) # join Unit Separator

def connect(self, auto=False, force=False):
    '''
        If `auto` is True, there will be no user interactions and everything will be done automatically,
        then there can be chosen by `force` what to do with the version mismatch.
        If `force` is True, connect() will connect to the server despite the version mismatch.
        Otherwise, if `force` is False, connect() will raise NotConnectedError when version mismatch occurs.
    '''
    if not self.test():
        if not auto:
            url.cookie = self.input('Authorization', 'Open ' + self.url+'/cookies.php' + ' and paste here what you get')
        if not self.test():
            raise NotConnectedError('Authorization fails')
    rv = self.version()
    if rv != self.PPSversion:
        if not (force or self.bool('Version mismatch', 'Your version of PPS is \''+self.PPSversion+'\' but version of chosen server\'s PPS is \''
                            +rv+'\'. Do you want to continue connecting to the server?')):
            raise NotConnectedError('User chose not to continue connecting to the server.')
        warnings.warn('Version mismatch (loc: '+self.PPSversion+'; rem: '+rv+')')

def inputfunc(title, msg):
    print(title, msg, sep='\n')
    return input()

def boolfunc(title, msg):
    print(title, str(msg)+' [type \'y\' to agree or \'n\' to disagree and press enter]:', sep='\n')
    s = ''
    while not (s == 'y' or s == 'n'):
        s = input()
    return True if s == 'y' else False
