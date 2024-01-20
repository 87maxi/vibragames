from base64 import b64encode, b64decode



class EncrytPasswd:

    salt = '%$1g1h2j3k'
    
    def encript_password(self, password):

        passwd = b64encode(str.encode(password+ self.salt))

        return passwd.decode("ascii")

    def decript_password(self, password):

        
        p= b64decode( password)
        passwd =  p.decode('ascii')
        passwd = passwd.replace(self.salt, '')
        return passwd
