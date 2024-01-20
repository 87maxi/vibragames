import hashlib



def encript_password(password):
    h = hashlib.shake_256(password.encode('ascii'))

    return h.hexdigest(20)


