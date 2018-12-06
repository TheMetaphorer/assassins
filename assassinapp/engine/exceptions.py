

class AuthenticationException(Exception):
    
    def __init__(self, msg):
        super(AuthenticationException, self).__init__(msg)