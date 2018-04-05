import string

from ciphers import Cipher


class Atbash(Cipher):
    """Encrypt a text message by mapping each letter to it's reverse, e.g. 'a'
    becomes 'z'.
    """

    def __init__(self):
        """Map each letter to it's reverse"""
        self.encrypt_mapping = {
            k: v for (k, v) in
            zip(Cipher.CHARACTERS, Cipher.CHARACTERS[::-1])
        }

    def encrypt(self, text):
        """return a new string, each letter of the string is the reverse of the
        corresponding letter in the original message.
        """
        return "".join([self.encrypt_mapping[letter] for letter in text])

    def decrypt(self, text):
        """Return the original message, the encrypted letters are restored"""
        return "".join(
            [k for l in text for k,
                v in self.encrypt_mapping.items() if v == l]
        )

