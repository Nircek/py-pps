#!/usr/bin/env python3

def url(uri):
    try:
        q = Request(uri)
        q.add_header('User-Agent', 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405')
        q.add_header('Cookie', url.cookie)
        return urlopen(q).read().decode()
    except Exception:
        print(uri)
        raise
url.cookie = '__test=c3495eae2f165b2aa28f8d430d413014 '

def perform(uri, cmd, params=()):
    args='?'
    for k, v in params.items():
        args += quote_plus(k) + '=' + quote_plus(v) + '&'
    args = args[:-1]
    return PPSReply(url(uri+'/'+cmd+'.php'+args)).exec()

def inputfunc(title, msg):
    print(title, msg, sep='\n')
    return input()

def boolfunc(title, msg):
    print(title, str(msg)+' [type \'y\' to agree or \'n\' to disagree and press enter]:', sep='\n')
    s = ''
    while not (s == 'y' or s == 'n'):
        s = input()
    return True if s == 'y' else False
