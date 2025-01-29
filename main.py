codeRange = 'abcdefghijklmnopqrstuvwxyz';
codeRangeLength = len(codeRange);
red = '\033[91m';
reset = '\033[0m';

def welcome():
    '''Display welcome message to the user.'''
    print(f"\n{reset}                        ___CEASER CIPHER___ \n                       ___BY SUWAN DHITAL___ \n---------------------------------------------------------------- \n Encrypt or Decrypt your File/Text using CeaserCipher Method... \n----------------------------------------------------------------");



def encryptOrDecrypt():
    '''Ask user to choose encryption or decryption
       Args: 
            None

       Returns:
            str: encrypt or decrypt as per user choice.
    '''
    while True:
        
        userInput = str.lower(input(f"\n{reset}Enter choice as per instruction: \n Press 'e' for Encryption. \n Press 'd' for Decryption.\n====================>{red}"));
       
        if userInput == 'e':
            return 'encrypt';
            break;
        elif userInput == 'd':
            return 'decrypt';
            break;
        else:
            print(f"{reset}PLEASE ENTER VALID CHOICE");

            
def message_or_file(task):
    '''Ask user to choose file or text that is need to be encrypted or decrypted.
       Args: 
            task(str): 'encrypt' or 'decrypt'.

       Returns:
            str: 'contents inside the file' or 'User entered text'.
            str: 'file' or 'text'.
    '''
    while True:
        userInput = input(f"\n{reset} Press 't' for text. \n Press 'f' for file. \n====================> {red}");
        if userInput == 'f':
            filePath = input(f"\n{reset}Enter Correct FileName:{red}");
            fileContent = process_file(filePath, task);
            return fileContent, 'file';
            break;
        elif userInput == 't':
            normalText = input(f"\n{reset}Enter Text for {task}ion:\n=>{red}");
            return normalText, 'text';
            break;
        else:
            print(f"{reset}PLEASE ENTER VALID CHOICE");

          
def process_file(fileName, task):
    '''Read the content of the file.
       Args: 
            fileName(str): Name of file.
            task(str): 'encrypt' or 'decrypt'.

       Returns:
            str: 'contents inside the file' or 'User entered text'.
    '''
    try:
        with open(fileName, 'r') as file:
            fileContent = file.read();
            return fileContent;

    except FileNotFoundError:
        print(f"{reset}FILE NOT FOUND");
        message_or_file(task);


def write_message(encryptedFileContent): 
    '''Read the content of the file.
       Args: 
            encryptedFileContent(str): encrypted contents that is retrived from the file.

    '''
    with open(f"result.txt", "w") as file:
        file.write(encryptedFileContent);
        print(f"{reset}Encrypted Text are stored in file named result.txt.");
    

def encrypt(normalText, key):
    ''' Encrypt the plain text
        Args:
            normalText(str): Text taken from user or file.
            key(str): Shift Key used to shift the value during encryption.
        Returns:
            encryptedText(str): encrypted text
    
    '''
    encryptedText = '';
    for letter in normalText:
        letter = letter.lower();
        if 'a' <= letter <= 'z':  
            letterPlace = codeRange.find(letter);
            replacedLetterPlace = (letterPlace + int(key)) % codeRangeLength;
            encryptedText += codeRange[replacedLetterPlace];
        else:
            encryptedText += letter;
    return encryptedText.upper();

        

def decrypt(encryptedText, key):
    ''' Decrypt the encrypted text
        Args:
            encryptedText(str): Text taken from user or file .
            key(str): Shift Key used to shift the value during decryption.
        Returns:
            normalText(str): decrypted text.
    
    '''
    normalText = '';
    for letter in encryptedText:
        letter = letter.lower();
        if 'a' <= letter <= 'z': 
                letterPlace = codeRange.find(letter);
                replacedLetterPlace = (letterPlace - int(key)) % codeRangeLength ;
                normalText += codeRange[replacedLetterPlace];
        else:
                normalText += letter;
    return normalText;

def loopTermination():
    ''' Logic to terminate the loop as per user choice.
         Returns:
            bool : True or False.
    '''
    while True:
            value = str.lower(input(f"\n{reset}-------------------------------------------------------\nWould you like to encrypt/decrypt another message? (y/n):{red}"));

            if(value == 'n'):
                print(f"\n{reset}-------------------------------------------------------\n      Thanks for using the program, Have a goodday....\n-------------------------------------------------------\n");
                return False;
                break;

            elif(value == 'y'):
                return True;
                break;
            else:
                print(f"{reset}INVALID INPUT")
                continue;

def shiftValue():
    ''' Take shift Key from user and return the value.
         Returns:
           key(str): Shifting Value required during encryption.
    '''
    while True:
      key = input(f"\n{reset}Enter the shift value:{red}");
      try:
        return key;  
        break;
      except ValueError:
          print(f"{reset}SHIFT KEY SHOULD BE NON-DECIMAL NEUMERICAL VALUE")
          continue;

              

def combineAll():
    ''' Main Function where all functions are segregated '''
    welcome();
    loop = True
    while loop:
        task = encryptOrDecrypt();
        choice = message_or_file(task);
        data ='';
        fileName ='';
        key = shiftValue();
        if task == 'encrypt':
            if choice[1] == 'file':
                data = encrypt(choice[0], key);
            elif choice[1] == 'text':
                data = encrypt(choice[0], key);
                  
        elif task == 'decrypt':
            if choice[1] == 'file':
                data = decrypt(choice[0], key);
            elif choice[1] == 'text':
                data = decrypt(choice[0], key);

        print(f"\n{reset}----------------------------------------------------------\n  Congrats, Your text has been {task}ed successfully.... \n----------------------------------------------------------");

        while True:
            saveOrView = str.lower(input(f"\n{reset} Press v to View. \n Press s to Save. \n Press b for Both. \n ====================>{red}"));
            if saveOrView == 'v':
                print(f"\n{reset}The {task}ed content of given {choice[1]} are: \n-------------------------------------------------------\n", data);
                break;

            elif saveOrView == 's':
               write_message(data);
               break
               

            elif saveOrView == 'b':
                print(f"\n{reset}The {task}ed content of given {choice[1]} are: \n-------------------------------------------------------\n", data);
                write_message(data);
                print(f"\n{reset}{task}ed data saved successfully...");
                break;
            else:
                print(f"{reset}INVALID INPUT")

        loop = loopTermination()

combineAll();
