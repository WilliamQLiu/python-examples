""" An example of an encryption algorithm (AES) """

from Crypto.Cipher import AES
import base64
import os

if __name__ == '__main__':

    BLOCK_SIZE = 32 # Block size for the cipher object must be 16, 24, 32 for AES

    PADDING = '*'

    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

    secret = os.urandom(BLOCK_SIZE)

    cipher = AES.new(secret)

    # Encode a string
    encoded = EncodeAES(cipher, '100000')
    print "Encrypted string:", encoded

    # Decode the encoded string
    decoded = DecodeAES(cipher, encoded)
    print "Decrypted string:", decoded
