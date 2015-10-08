"""
File: crypto.py
Name: Matt Mahowald
Date: October 9th 2015
Description: crypto.py implements a cryptography suite that allows
the user to input a message or a filename and then either encrypt 
or decrypt the message
"""

NUM_ALPHA_LETTERS = 26

def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    Add more implementation details here.
    """
    caesar_offset = 3
    new_string = ""
    uppertext = plaintext.upper()
    for letter in uppertext:
        if(letter.isalpha()):
            if((ord(letter) + caesar_offset) <= ord('Z')):
                new_string += chr((ord(letter) + caesar_offset))
            else:
                new_string += chr((ord(letter) - NUM_ALPHA_LETTERS + caesar_offset))
    return new_string

def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    Add more implementation details here.
    """
    new_string = ""
    uppertext = ciphertext.upper()
    for letter in uppertext:
        if(letter.isalpha()):
            if((ord(letter) + 3) < ord('Z')):
                new_string += chr((ord(letter) + 3))
            else:
                new_string += chr((ord(letter) - 23))
    return new_string

def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher with a keyword.
    Add more implementation details here.
    """
    new_string = ""
    for i in range(len(plaintext)):
        key_char = keyword[i % len(keyword)]
        new_chr = chr(ord(plaintext[i]) + ord(key_char) - ord('A'))
        if(not new_chr.isalpha()):
            new_chr = chr(ord(new_chr) - 26)
        new_string += new_chr
    return new_string

def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts ciphertext using a Vigenere cipher with a keyword.
    Add more implementation details here.
    """
    new_string = ""
    for i in range(len(ciphertext)):
        key_char = keyword[i % len(keyword)]
        new_chr = chr(ord(ciphertext[i]) + ord('A') - ord(key_char))
        if(not new_chr.isalpha()):
            new_chr = chr(ord(new_chr) + 26)
        new_string += new_chr
    return new_string
    
def encrypt_railfence(plaintext, num_rails):
    """
    Encrypts plaintext using a railfence cipher.
    Add more implementation details here.
    """
    rails = ["" for i in range(num_rails)]
    print(rails)
   
    row = 0
    d = 1
    for ch in plaintext:
        if(not ch.isalpha()): continue
        rails[row] = rails[row] + ch
        row += d
        if row == num_rails:
           d = -1
           row -= 2
        if row == -1:
           d = 1
           row += 2 
    print(rails)
    return "".join(rails)


def decrypt_railfence(ciphertext, num_rails):
    """
    Encrypts plaintext using a railfence cipher.
    Add more implementation details here.
    """
    pass  # Your implementation here

def read_from_file(filename):
    """
    Reads and returns content from a file.
    Add more implementation details here.
    """
    pass  # Your implementation here

def write_to_file(filename, content):
    """
    Writes content to a file.
    Add more implementation details here.
    """
    pass  # Your implementation here


def get_keyword():
    return input("Enter a keyword: ").upper()

def get_nrails():
    return int(input("Enter an integer: "))

def transform_text(raw_text, operation, tool):
    print("*Output*") 
    if(operation == 'E'):
        if(tool == 'C'):
            return encrypt_caesar(raw_text)
        elif(tool == 'V'):
            return encrypt_vigenere(raw_text, get_keyword())
        elif(tool == 'R'):
            return encrypt_railfence(raw_text, get_nrails())
    elif(operation == 'D'):
        if(tool == 'C'):
            return decrypt_caesar(raw_text)
        elif(tool == 'V'):
            return decrypt_vigenere(raw_text, get_keyword())
        elif(tool == 'R'):
            return encrypt_railfence(raw_text, get_nrails())
    else:
        print("We're sorry, an error has occurred")

def prompt_for_filename():
    return input('Please enter a valid filename: ')

def run_suite():
    """
    Runs a single iteration of the cryptography suite.

    Asks the user for input text from a string or file, whether to encrypt
    or decrypt, what tool to use, and where to show the output.
    """

    raw_text = "" # Variable for the to-be-encrypted/decrypted text 
    if(input_type_is_file()):
        filename = prompt_for_filename()
        raw_text = read_from_file(filename)
    else:
        raw_text = input("Enter the string to encrypt or decrypt: ").upper()
    operation = transformation_type()
    tool = encryption_method() 
    message = transform_text(raw_text, operation, tool)
    print(message)

def encryption_method():
    input_type = input("(C)aesar, (V)igenere, or (R)ailfence? ").upper()
    while not input_type or input_type[0] not in ['C', 'V', 'R']:
        input_type = input("Please enter either 'C', 'V', or 'R': ").upper()
    return input_type[0]  

def transformation_type():
    print("*Transform*")
    input_type = input("(E)ncrypt or (D)ecrypt? ").upper()
    while not input_type or input_type[0] not in ['E', 'D']:
        input_type = input("Please enter either 'E' or 'D': ").upper()
    return input_type[0]

def input_type_is_file():
    print("*Input*")
    input_type = input("(F)ile or (S)tring? ").upper()
    while not input_type or input_type[0] not in ['F', 'S']:
        input_type = input("Please enter either 'F' or 'S': ").upper()
    return input_type[0] == 'F'

# Do not modify code beneath this point.
def should_continue():
    """
    Asks the user whether they would like to continue.
    Responses that begin with a `Y` return True. (case-insensitively)
    Responses that begin with a `N` return False. (case-insensitively)
    All other responses (including '') cause a reprompt.
    """
    choice = input("Again (Y/N)? ").upper()
    while not choice or choice[0] not in ['Y', 'N']:
        choice = input("Please enter either 'Y' or 'N'. Again (Y/N)? ").upper()
    return choice[0] == 'Y'


def main():
    """Harness for the Cryptography Suite"""
    print("Welcome to the Cryptography Suite!")
    run_suite()
    while should_continue():
        run_suite()
    print("Goodbye!")


if __name__ == '__main__':
    """This block is run if and only if the Python script is invoked from the
    command line."""
    main()
