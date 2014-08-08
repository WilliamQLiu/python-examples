""" Testing out how to use the hashlib library
    Can be used to validate cookies (e.g. visits, users)

 """

import hashlib
import hmac

def hash_str_md5(text):
    """ h(1) = hash, quick but not quite as secure """
    x = hashlib.md5(text)
    print "MD5 hexdigest is: " + x.hexdigest()

def hash_str_sha256(text):
    """ h(1) = hash, slower but more secure """
    x = hashlib.sha256(text)
    print "Sha256 hexdigest is: " + x.hexdigest()

def hmac_str(text):
    """ h(secret + 1) = hash  <<< basically use this """
    x = hmac.new("thisismysecret", text).hexdigest()
    print "HMAC hexdigest is: " + x

if __name__ == '__main__':
    hash_str_md5("Hello world")
    hash_str_sha256("Hello world")
    hmac_str("Hello world")
