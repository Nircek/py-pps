#!/usr/bin/env python3

class NotConnectedError(Exception):
    pass

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
