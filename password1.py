import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8)
    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('utf-8')
    assert isinstance(password, str)

    for i in range(10):
        encrypted = HMAC(password, salt, sha256).digest()
    return salt + encrypted


def validate_password(hashed, password):
    return hashed == encrypt_password(password, hashed[:8])


if __name__ == "__main__":
    password_new = raw_input("Set your password\n")
    password_saved = encrypt_password(password_new)
    password_again = raw_input("Now,type in your password\n")
    print "Password match." if validate_password(password_saved, password_again) else "wrong password."
