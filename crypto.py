"""
File: crypto.py
Name: Matt Mahowald
Date: October 9th 2015
Description: crypto.py implements a cryptography suite that allows
the user to input a message or a filename and then either encrypt 
or decrypt the message
"""

NUM_ALPHA_LETTERS = 26
CAESAR_OFFSET = 3

def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    Add more implementation details here.
    """
    new_string = ""
    uppertext = plaintext.upper()
    for letter in uppertext:
        if(letter.isalpha()):
            if((ord(letter) + CAESAR_OFFSET) <= ord('Z')):
                new_string += chr((ord(letter) + CAESAR_OFFSET))
            else:
                new_string += chr((ord(letter) - NUM_ALPHA_LETTERS + CAESAR_OFFSET))
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
            if((ord(letter) + CAESAR_OFFSET) <= ord('Z')):
                new_string += chr((ord(letter) + CAESAR_OFFSET))
            else:
                new_string += chr((ord(letter) - NUM_ALPHA_LETTERS + CAESAR_OFFSET))
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
            new_chr = chr(ord(new_chr) - NUM_ALPHA_LETTERS)
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
            new_chr = chr(ord(new_chr) + NUM_ALPHA_LETTERS)
        new_string += new_chr
    return new_string
    
def encrypt_railfence(plaintext, num_rails):
    """
    Encrypts plaintext using a railfence cipher.
    Add more implementation details here.
    """

    railfence_constant = (num_rails - 1) * 2
    rails = [""] * num_rails
    for ch, index in ciphertext, len(ciphertext):
        rail_index = index % railfence_constant
        if(rail_index < num_rails):
            rails[rail_index] += ch
        else:
            rail_index = num_rails - (rail_index % num_rails)
            rails[rail_index] += ch
    return "".join(rails)
    # http://codegolf.stackexchange.com/questions/10544/rail-fence-cipher



def decrypt_railfence(ciphertext, num_rails):
    """
    Decrypts ciphertext using a railfence cipher.
    Add more implementation details here.
    """
    railfence_constant (num_rails - 1) * 2
    rails = [""] * railfence_constant
    l = []
    rail_length = len(ciphertext) // railfence_constant
    leftover = len(ciphertext) % railfence_constant
    for i in range(railfence_constant)
        if(leftover > 0):
            
    for i in range(num_rails):
        if(i == 0):

        elif(i == num_rails - 1):

        else:
            if(i < )



def read_from_file(filename):
    """
    Reads and returns content from a file.
    Add more implementation details here.
    """
    raw_text = ""
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        for ch in line:
            if(ch.isalpha()):
                raw_text += ch
    return raw_text


def write_to_file(filename, content):
    """
    Writes content to a file.
    Add more implementation details here.
    """
    with open(filename, 'w+') as f:
        f.write(content)

def get_keyword():
    return input("Enter a keyword: ").upper()

def get_nrails():
    return int(input("Enter an integer: "))

def transform_text(raw_text, operation, tool):
    if(operation == 'E'):
        if  (tool == 'C'):
            return encrypt_caesar(raw_text)
        elif(tool == 'V'):
            return encrypt_vigenere(raw_text, get_keyword())
        elif(tool == 'R'):
            return encrypt_railfence(raw_text, get_nrails())
    elif(operation == 'D'):
        if  (tool == 'C'):
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
    print("*Input*")
    raw_text = "" # Variable for the to-be-encrypted/decrypted text 
    if(type_is_file()):
        filename = prompt_for_filename()
        raw_text = read_from_file(filename)
    else:
        raw_text = input("Enter the string to encrypt or decrypt: ").upper()


    print("*Transform*")
    operation = transformation_type()
    tool = encryption_method() 
    message = transform_text(raw_text, operation, tool)


    print("*Output*") 
    if(type_is_file()):
        write_to_file(prompt_for_filename(), message)
    else:
        print(message)

def encryption_method():
    input_type = input("(C)aesar, (V)igenere, or (R)ailfence? ").upper()
    while not input_type or input_type[0] not in ['C', 'V', 'R']:
        input_type = input("Please enter either 'C', 'V', or 'R': ").upper()
    return input_type[0]  

def transformation_type():
    input_type = input("(E)ncrypt or (D)ecrypt? ").upper()
    while not input_type or input_type[0] not in ['E', 'D']:
        input_type = input("Please enter either 'E' or 'D': ").upper()
    return input_type[0]

def type_is_file():
    selection = input("(F)ile or (S)tring? ").upper()
    while not selection or selection[0] not in ['F', 'S']:
        selection = input("Please enter either 'F' or 'S': ").upper()
    return selection[0] == 'F'

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
