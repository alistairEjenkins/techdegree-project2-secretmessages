import random
import string

class Cipher:

    CHARACTERS = string.ascii_lowercase + '0123456789'

    def __init__(self):

       self.letter_mapping = {k: v for (k, v) in zip(string.printable, range(100))}

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

