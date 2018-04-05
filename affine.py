import string

from ciphers import Cipher


class Affine(Cipher):
    """Encrypt text by,
    1. Map each letter of a message to their ordinal positional number in the
    alphabet.
    2. Pass these ordinal numbers through a function to generate a different
    ordinal number.
    3. Re-map each number to the alphabet
    """
    def __init__(self):
        """Map letters to their ordinal position in alphabet, a to 0; b to 1;
        ...; z to 25
        """
        self.letter_mapping = {
            k: v for (k, v) in zip(Cipher.CHARACTERS, range(36))
        }

    def encrypt(self, text):
        """Encrypt text by generating a list of new ordinal values then map
        these numbers to letters
        """
        ordinals = [self.encrypt_equation(x) for x in text]
        return ''.join(self.map_numbers_to_letters(ordinals))

    def encrypt_equation(self, letter):
        """Equation for generating new ordinal number when encrypting."""
        return (5 * self.letter_mapping[letter] + 8) % 36

    def map_numbers_to_letters(self, map):
        """Map ordinal positions to their corresponding letter"""
        return [
            k for num in map for k, v in self.letter_mapping.items()if v == num
        ]

    def decrypt(self, text):
        """Decrypt text by generating new ordinal values then map these
        numbers to letters
        """
        mapping = [self.decrypt_equation(letter) for letter in text]
        return ''.join(self.map_numbers_to_letters(mapping))

    def decrypt_equation(self, letter):
        """Equation for generating new ordinal number when decrypting."""
        return (29 * (self.letter_mapping[letter] - 8)) % 36

