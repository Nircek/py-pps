#!/usr/bin/env python3
from enum import Enum

class PPSCodeException(Exception):
    pass

class PPSError(PPSCodeException):
    pass

class PPSDBError(PPSCodeException):
    pass

class PPSUnexpectedError(PPSCodeException):
    pass

'''
1   Not enough parameters in the request
2   User privileges denied
3   Admin privileges denied
4   Log file problem
5   No elements in the queue
6   A user with the same login exists
'''
class PPSParameterError(PPSError):
    pass

class PPSUserDeniedError(PPSError):
    pass

class PPSAdminDeniedError(PPSError):
    pass

class PPSLogError(PPSError):
    pass

class PPSNullError(PPSError):
    pass

class PPSSameUserError(PPSError):
    pass

class PPSUnsupportedError(PPSError):
    pass

class PPSCode(Enum):
    GOOD = 0
    ERROR = 1
    DBERROR = 2
    UNEXPECTEDERROR = 3
    def get(s):
        d = {'0': PPSCode.GOOD, '-': PPSCode.ERROR, '+': PPSCode.DBERROR}
        return PPSCode.UNEXPECTEDERROR if len(s) == 0 or not s[0] in d else d[s[0]]
    def __bool__(self):
        return self == PPSCode.GOOD

class PPSReply:
    def __init__(self, s):
        s=s.rstrip('\r\n')
        self.type = PPSCode.get(s)
        if self.type != PPSCode.UNEXPECTEDERROR:
            s = s[1:]
        self.args = s.split('\N{Symbol For Unit Separator}')
    def exec(self):
        c = PPSDBError if self.type == PPSCode.DBERROR else PPSUnexpectedError
        if self.type == PPSCode.ERROR:
            d = { '1': PPSParameterError,
                  '2': PPSUserDeniedError,
                  '3': PPSAdminDeniedError,
                  '4': PPSLogError,
                  '5': PPSNullError,
                  '6': PPSSameUserError}
            c = d[self.args[0]] if self.args[0] in d else PPSUnsupportedError
        if self.type:
            return self.args
        else:
            raise c(self.args)
    def __repr__(self):
        return 'PPSReply' + repr((self.type, self.args))

def url(uri):
    q = Request(uri)
    q.add_header('User-Agent', 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405')
    q.add_header('Cookie', url.cookie)
    return urlopen(q).read().decode()
url.cookie = '__test=eb93faad212ed7dc5ddc4a144182d12d '

def inputfunc(title, msg):
    print(title, msg, sep='\n')
    return input()
