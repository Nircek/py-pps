#!/usr/bin/env python3
from enum import Enum

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
    def __bool__(self):
        return self == PPSCode.GOOD

class PPSReply:
    def __init__(self, s):
        s=s.rstrip('\r\n')
        self.type = PPSCode.get(s)
        if self.type != PPSCode.UNEXPECTEDERROR:
            s = s[1:]
        self.args = s.split('\N{Symbol For Unit Separator}')
    def __repr__(self):
        return 'PPSReply' + repr((self.type, self.args))
