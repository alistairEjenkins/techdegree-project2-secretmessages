import random
from ciphers import Cipher


class One_time_pad():

    def __init__(self):

        self.letter_mapping = {
            k: v for (k, v) in zip(Cipher.CHARACTERS, range(36))
        }

    def encrypt(self, message):

        m_ords, k_ords = self.set_ordinals(message)
        encrypted_ordinals = [(m_ords[i] + k_ords[i]) % 36
                              for i in range(len(message))]

        return ''.join(self.map_numbers_to_letters(encrypted_ordinals))

    def decrypt(self, message):

        m_ords, k_ords = self.set_ordinals(message)
        decrypted_ordinals = [(m_ords[i] - k_ords[i]) % 36
                              for i in range(len(message))]

        return ''.join(self.map_numbers_to_letters(decrypted_ordinals))

    def set_ordinals(self, message):
        message_ordinals = [self.letter_mapping[letter] for letter in message]
        key_ordinals = [self.letter_mapping[letter]
                        for letter in input('What is your key? ')]

        return message_ordinals, key_ordinals

    def map_numbers_to_letters(self, map):
        """Map ordinal positions to their corresponding letter"""
        return [
            k for num in map for k, v in self.letter_mapping.items()
            if v == num
              ]

