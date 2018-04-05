import os
import sys
from affine import Affine
from atbash import Atbash
from polybius import Polybius
from ciphers import Cipher
from one_time_pad import One_time_pad


def menu():
    """Create a simple menu where the user is prompted to
    1. Choose a cipher,
    2. Input a message,
    3. Encrypt or decrypt that message according to the chosen cipher,
    4. Give the user an option to encode message further, adding
        a 'one time pad'
    """
    while True:

        draw_menu()
        clear_screen()

        ciphers = {'1': Affine, '2': Atbash, '3': Polybius}
        while True:
            try:
                # user chooses a cipher from selection
                cipher = ciphers[input('Which cipher would you like to use'
                                       ', 1/2/3? '
                                       )]
            except KeyError:
                print('I did not recognise your choice. Please try again.')
                continue
            else:
                cipher_chosen = cipher()
                # space character is added to ciphers character set if Polybius
                # cipher is chosen
                if cipher == Polybius:
                    Cipher.CHARACTERS += ' '
                break

        while True:

            # user supplies message
            message = input('What is your message? ')
            for letter in message:
                if letter not in Cipher.CHARACTERS:
                    print('I did not understand your message.'
                          'Please input again. '
                          )
                    break
            else:
                break
        encodes = {'e': cipher_chosen.encrypt, 'd': cipher_chosen.decrypt}

        while True:
            try:
                # the user chooses whether to encrypt or decrypt their message
                encode_choice = encodes[input('Do you want to encrypt (e)'
                                              'or decrypt (d) your message?')
                                        .lower()]
            except KeyError:
                print('I did not recognise your choice. Please try again.')
            else:
                break

        # encrypt/decrypt message under chosen cipher,
        # one time pad optional against Affine and Atbash ciphers
        if cipher == Polybius:
            print(encode_choice(message))
        else:
            pad = input('Do you wish to include a one time pad? Y/n').lower()
            if pad != 'n':
                o = One_time_pad()
                if encode_choice == cipher_chosen.encrypt:
                    # encrypted messages are displayed 5 characters at a time
                    print(
                        'Here is your encrypted message : {}'.
                        format(group_by_five(o.encrypt
                                             (encode_choice(message)))))
                else:
                    print('Here is your decrypted message : {}'.
                          format(encode_choice(o.decrypt(message))))
            else:
                print('Here is your encoded message : {}'.
                      format(encode_choice(message)))

        encode_another_message = input('Do you want to encode '
                                       'a further message Y/n').lower()
        if encode_another_message != 'n':
            continue
        else:
            sys.exit()


def draw_menu():
    # prints welcome message and menu
    print(
        'This is the Secret messages project for Treehouse Techdegree.\n'
    )
    print('These are the available ciphers:\n')
    print('1 - Affine')
    print('2 - Atbash')
    print('3 - Polybius\n\n')


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def group_by_five(message):
    grouped_message = ''
    for i in range(0, len(message), 5):
        grouped_message += message[i:i + 5] + ' '

    return grouped_message


def main():
    menu()


if __name__ == '__main__':
    main()

