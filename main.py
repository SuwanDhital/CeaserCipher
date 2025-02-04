CODE_RANGE = 'abcdefghijklmnopqrstuvwxyz'
CODE_RANGE_LENGTH = len(CODE_RANGE)
RED = '\033[91m'
RESET = '\033[0m'

def welcome():
    '''Display welcome message to the user.'''
    print(f"\n{RESET}                        ___CEASER CIPHER___ \n")
    print("                       ___BY SUWAN DHITAL___ \n")
    print("---------------------------------------------------------------- \n")
    print(" Encrypt or Decrypt your File/Text using CeaserCipher Method... \n")
    print("----------------------------------------------------------------")


def encrypt_or_decrypt():
    '''Ask user to choose encryption or decryption
       Args: 
            None

       Returns:
            str: encrypt or decrypt as per user choice.
    '''
    while True:
        print(f"\n{RESET}Enter choice as per instruction:\n Press 'e' for Encryption.")
        print("\n Press 'd' for Decryption.\n")
        user_input = str.lower(input(f"====================>{RED}"))

        if user_input == 'e':
            return 'encrypt'
        if user_input == 'd':
            return 'decrypt'

        print(f"{RESET}PLEASE ENTER VALID CHOICE")

def enter_message(task):
    '''Ask user to choose file or text that is need to be encrypted or decrypted.
       Args: 
            task(str): 'encrypt' or 'decrypt'.

       Returns:
            str: 'contents inside the file' or 'User enteRED text'.
            str: 'file' or 'text'.
    '''
    while True:
        print(f"\n{RESET} Press 't' for text. \n Press 'f' for file. \n")
        user_input = input(f"====================> {RED}")
        if user_input == 'f':
            file_path = input(f"\n{RESET}Enter Correct FileName:{RED}")
            file_content = process_file(file_path, task)
            return file_content, 'file'

        if user_input == 't':
            normal_text = input(f"\n{RESET}Enter Text for {task}ion:\n=>{RED}")
            return normal_text, 'text'
        print(f"{RESET}PLEASE ENTER VALID CHOICE")

def process_file(file_name, task):
    '''Read the content of the file.
       Args: 
            file_name(str): Name of file.
            task(str): 'encrypt' or 'decrypt'.

       Returns:
            str: 'contents inside the file' or 'User enteRED text'.
    '''
    try:
        with open(file_name, 'r',encoding='utf-8') as file:
            file_content = file.read()
            return file_content

    except FileNotFoundError:
        print(f"{RESET}FILE NOT FOUND")
        enter_message(task)


def write_message(encrypted_file_content):
    '''Read the content of the file.
       Args: 
            encrypted_file_content(str): encrypted contents that is retrived from the file.
    '''
    with open("result.txt", "w",encoding='utf-8') as file:
        file.write(encrypted_file_content)
        print(f"{RESET}Encrypted Text are stoRED in file named result.txt.")

def encrypt(normal_text, key):
    ''' Encrypt the plain text
        Args:
            normal_text(str): Text taken from user or file.
            key(str): Shift Key used to shift the value during encryption.
        Returns:
            encrypted_text(str): encrypted text
    '''
    encrypted_text = ''
    for letter in normal_text:
        letter = letter.lower()
        if 'a' <= letter <= 'z':  
            letter_place = CODE_RANGE.find(letter)
            replaced_letter_place = (letter_place + int(key)) % CODE_RANGE_LENGTH
            encrypted_text += CODE_RANGE[replaced_letter_place]
        else:
            encrypted_text += letter
    return encrypted_text.upper()

def decrypt(encrypted_text, key):
    ''' Decrypt the encrypted text
        Args:
            encrypted_text(str): Text taken from user or file .
            key(str): Shift Key used to shift the value during decryption.
        Returns:
            normal_text(str): decrypted text.
    
    '''
    normal_text = ''
    for letter in encrypted_text:
        letter = letter.lower()
        if 'a' <= letter <= 'z': 
            letter_place = CODE_RANGE.find(letter)
            replaced_letter_place = (letter_place - int(key)) % CODE_RANGE_LENGTH 
            normal_text += CODE_RANGE[replaced_letter_place]
        else:
            normal_text += letter
    return normal_text

def loop_terminator():
    ''' Logic to terminate the loop as per user choice.
         Returns:
            bool : True or False.
    '''
    while True:
        print("\n{RESET}-------------------------------------------------------\n")
        value = str.lower(input(f"Would you like to encrypt/decrypt another message? (y/n):{RED}"))

        if value == 'n':
            print(f"\n{RESET}-------------------------------------------------------\n")
            print("      Thanks for using the program, Have a goodday....\n")
            print("-------------------------------------------------------\n")
            return False
        if value == 'y':
            return True
        print(f"{RESET}INVALID INPUT")
        continue

def shift_value():
    ''' Take shift Key from user and return the value.
         Returns:
           key(str): Shifting Value requiRED during encryption.
    '''
    while True:
        key = input(f"\n{RESET}Enter the shift value:{RED}")
        try:
            return key
        except ValueError:
            print(f"{RESET}SHIFT KEY SHOULD BE NON-DECIMAL NEUMERICAL VALUE")
            continue           

def main():
    ''' Main Function where all functions are segregated '''
    welcome()
    loop = True
    while loop:
        task = encrypt_or_decrypt()
        choice = enter_message(task)
        data =''
        key = shift_value()
        if task == 'encrypt':
            if choice[1] == 'file':
                data = encrypt(choice[0], key)
            elif choice[1] == 'text':
                data = encrypt(choice[0], key) 
        elif task == 'decrypt':
            if choice[1] == 'file':
                data = decrypt(choice[0], key)
            elif choice[1] == 'text':
                data = decrypt(choice[0], key)
        print(f"\n{RESET}----------------------------------------------------------\n")
        print(f"  Congrats, Your text has been {task}ed successfully.... \n")
        print("----------------------------------------------------------")

        while True:
            print(f"\n{RESET} Press v to View. \n Press s to Save. \n")
            save_or_view = str.lower(input(f" Press b for Both. \n ====================>{RED}"))
            if save_or_view == 'v':
                print(f"\n{RESET}The {task}ed content of given {choice[1]} are:")
                print(" \n-------------------------------------------------------\n", data)
                break
            if save_or_view == 's':
                write_message(data)
                break
            if save_or_view == 'b':
                print(f"\n{RESET}The {task}ed content of given {choice[1]} are: ")
                print("\n-------------------------------------------------------\n", data)
                write_message(data)
                print(f"\n{RESET}{task}ed data saved successfully...")
                break
            print(f"{RESET}INVALID INPUT")
        loop = loop_terminator()

main()
