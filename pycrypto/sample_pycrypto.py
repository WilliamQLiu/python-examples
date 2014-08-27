""" An example of an encryption algorithm (AES)
    Advanced Encryption Standard is a symmetric block cipher
    It has a fixed data block size of 16 bytes
    Its keys can be 128, 192, or 256 bits long

 """

from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import os


if __name__ == '__main__':

    BLOCK_SIZE = 32 # Block size for the cipher object must be 16, 24, 32 for AES

    PADDING = '*'

    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

    EncodeAES = lambda c, s: b64encode(c.encrypt(pad(s)))
    DecodeAES = lambda c, e: c.decrypt(b64decode(e)).rstrip(PADDING)

    secret = os.urandom(BLOCK_SIZE)

    cipher = AES.new(secret)

    # Encode a string
    encoded = EncodeAES(cipher, "This is the text I'm encoding")
    print "Encrypted string:", encoded

    # Decode the encoded string
    decoded = DecodeAES(cipher, encoded)
    print "Decrypted string:", decoded
