import string

from ciphers import Cipher


class Polybius(Cipher):
    """Encrypt text by turning each character of a message into a two digit
    number representing the x and y coordinates of a table where matching
    letters of the alphabet are stored.
    """

    # characters to be stored in Polybius table
    CHARACTERS = string.ascii_lowercase + '0123456789'

    def __init__(self):

        # initialise polybius table coordinates
        self.coords = [(x, y) for x in range(6) for y in range(6)]
        # create mappings for message letters to table coordinates and
        # vica-versa
        self.encrypt_mapping = {k: v for (k, v) in zip(
            Cipher.CHARACTERS, self.coords)}
        self.decrypt_mapping = {k: v for (k, v) in zip(
            self.coords, Cipher.CHARACTERS)}

    def encrypt(self, text):
        """Turn letters into numbers representing coordinates of the table"""
        output = [
            str(self.encrypt_mapping[l][0]) +
            str(self.encrypt_mapping[l][1]) for l in text
            ]

        return ' '.join(output)

    def decrypt(self, text):
        """Turn two digit numbers into the corresponding letter in the Polybius
        table at the x,y coordinates of those digits
        """
        output = [
            self.decrypt_mapping[(int(letter[0]), int(letter[1]))]
            for letter in text.split(' ')
            ]
        return ''.join(output)

