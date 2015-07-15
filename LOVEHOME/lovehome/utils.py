import re
import hashlib
import hmac

class signup_login:
    def __init__(self):
        self.username_info    = ''
        self.password_info    = ''
        self.error_info       = ''
        self.secret           = b'Marvell101_rdou'
        self.username_pattern = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
        self.password_pattern = re.compile(r'^.{3,20}$')
    
    def valid_username(self, username):
        return self.username_pattern.match(username)
    
    def valid_password(self, password):
        return self.password_pattern.match(password)
    
    def make_secure_value(self, s):
        return '%s' % (hmac.new(self.secret, s).hexdigest())

    def check_secure_val(self, h, p):
        if h == self.make_secure_value(p):
            return True
        else:
            return False
    
    def check_signup(self, username, password):
        _valid_username = self.valid_username(username) 
        _valid_password = self.valid_password(password)
        
        if not _valid_username:
            self.username_info = 'Wrong username format !!!'
        if not _valid_password:
            self.password_info = 'Wrong password format !!!'
        if _valid_password and _valid_username:
            return True
        else:
            return False

