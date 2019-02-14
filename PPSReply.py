#!/usr/bin/env python3
from enum import Enum
from .PPSExceptions import *

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
