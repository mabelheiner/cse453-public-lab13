##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        # TODO: Insert anything you need for your cipher here
        pass

    def get_author(self):
        # TODO: Return your name
        return "Mabel Heiner"

    def get_cipher_name(self):
        # TODO: Return the cipher name
        return "Vigenère cipher"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        # TODO: This function should return your citation(s)
        return "Vigenère Cipher - Khanduri, A. (2023, May 29). Vigenère Cipher. GeeksforGeeks. https://www.geeksforgeeks.org/vigenere-cipher/# "

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # TODO: This function should return your psuedocode, neatly formatted

        # The encrypt pseudocode
        pc = """Encryption Pseudocode: 
        \tInitialize an empty string to store the encrypted text
        Convert the password to uppercase for consistency
        Repeat the password to match the length of the plaintext, using modular arithmetic
        Iterate through each character in the plaintext:
            If the character is a letter:
                Shift it by the corresponding letter in the password
                Wrap around the alphabet if necessary
                Append the encrypted character to the result string
            If the character is not a letter, shift it around to the corresponding number
                Append the encrypted character to the result string
        Return the encrypted text\n"""

        # The decrypt pseudocode
        pc += """Decryption Pseudocode: 
        \tInitialize an empty string to store the decrypted text
        Convert the password to uppercase for consistency
        Repeat the password to match the length of the encrypted text, using modular arithmetic
        Iterate through each character in the encrypted text:
            If the character is a letter:
                Shift it back by the corresponding letter in the password
                Wrap around the alphabet if necessary
                Append the decrypted character to the result string
            If the character is not a letter, shift it back to the digit in the password
                Append the decrypted character to the result string
        Return the decrypted text\n"""

        return pc

    ##########################################################################
    # ENCRYPT
    # TODO: ADD description
    ##########################################################################
    def encrypt(self, plaintext, password):
        ciphertext = ''
        password = password.upper()
        password_length = len(password)
        for i, char in enumerate(plaintext):
            if char.isalpha():
                shift = ord(password[i % password_length]) - ord('A')
                if char.islower():
                    encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif char.isdigit():
                shift = ord(password[i % password_length]) - ord('A')  
                encrypted_char = chr((ord(char) - ord('0') + shift) % 10 + ord('0'))  
            else:
                encrypted_char = char  
            ciphertext += str(encrypted_char)
        return ciphertext


    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, ciphertext, password):
        plaintext = ''
        password = password.upper()
        password_length = len(password)

        for i, char in enumerate(ciphertext):
            if char.isalpha():
                shift = ord(password[i % password_length]) - ord('A')
                if char.islower():
                    decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
                else:
                    decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            elif char.isdigit():
                shift = ord(password[i % password_length]) - ord('A')
                decrypted_char = chr((ord(char) - ord('0') - shift + 10) % 10 + ord('0'))
            else:
                decrypted_char = char
            plaintext += str(decrypted_char)
        return plaintext
