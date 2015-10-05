"""
File: crypto.py
Name: Matt Mahowald
Date: October 9th 2015
"""

def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    Add more implementation details here.
    """
    new_string = ""
    uppertext = plaintext.upper()
    for letter in uppertext:
        if(letter.isalpha()):
            if(chr((ord(letter) + 4)).isalpha()):
                new_string += chr((ord(letter) + 3))
            else:
                new_string += chr((ord(letter) - 23))
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
            new_string += chr((ord(letter) - 4))
    return new_string


def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher with a keyword.
    Add more implementation details here.
    """
    pass  # Your implementation here


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts ciphertext using a Vigenere cipher with a keyword.
    Add more implementation details here.
    """
    pass  # Your implementation here


def encrypt_railfence(plaintext, num_rails):
    """
    Encrypts plaintext using a railfence cipher.
    Add more implementation details here.
    """
    pass  # Your implementation here

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

def transform_text(raw_text, operation, tool):
    print("*Output*") 
    if(operation == 'E'):
        if(tool == 'C'):
            return encrypt_caesar(raw_text)
        elif(tool == 'V'):
            return "Not Implemented!"
        elif(tool == 'R'):
            return "Not Implemented!"
    elif(operation == 'D'):
        if(tool == 'C'):
            return decrypt_caesar(raw_text)
        elif(tool == 'V'):
            return "Not Implemented!"
        elif(tool == 'R'):
            return "Not Implemented!"
    else:
        print("We're sorry, an error has occurred")

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
        raw_text = input("Enter the string to encrypt or decrypt: ")
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
