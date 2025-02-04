# Caesar Cipher

## Overview

The Caesar Cipher is a simple and well-known encryption technique that shifts the letters of the alphabet by a fixed number of places. This project allows users to encrypt or decrypt text or files using the Caesar Cipher method. The program is designed to be user-friendly and provides options for both text input and file input.

## Features

- Encrypt and decrypt text using the Caesar Cipher method.
- Support for both direct text input and file input.
- User-friendly interface with clear instructions.
- Option to view the encrypted/decrypted content or save it to a file.
- Handles non-alphabetic characters gracefully.

## Requirements

- Python 3.x
- Basic understanding of command-line interface

## Installation

1. Clone the repository or download the code files.
2. Ensure you have Python 3 installed on your machine.
3. Navigate to the directory containing the code files.

## Usage

1. Run the program using the command:
   ```bash
   python main.py
   ```
   (Replace `main.py` with the actual filename if different.)

2. Follow the on-screen instructions:
   - Choose whether you want to encrypt or decrypt.
   - Select whether you want to input text directly or from a file.
   - If using a file, provide the correct filename.
   - Enter the text or the shift value as prompted.

## Example of Running the Code

### Example 1: Encrypting Text

1. **Run the program:**
   ```bash
   python mainr.py
   ```

2. **Choose encryption:**
   ```
   Enter choice as per instruction:
   Press 'e' for Encryption.
   Press 'd' for Decryption.
   =====================> e
   ```

3. **Choose text input:**
   ```
   Press 't' for text.
   Press 'f' for file.
   =====================> t
   ```

4. **Enter the text to encrypt:**
   ```
   Enter Text for encryption:
   => Hello World
   ```

5. **Enter the shift value:**
   ```
   Enter the shift value: 3
   ```

6. **View or save the encrypted content:**
   ```
   Press v to View.
   Press s to Save.
   Press b for Both.
   ======================> v
   ```

7. **Output:**
   ```
   The encrypted content of given text are:
   -------------------------------------------------------
   Khoor Zruog
   ```

### Example 2: Decrypting a File

1. **Run the program:**
   ```bash
   python caesar_cipher.py
   ```

2. **Choose decryption:**
   ```
   Enter choice as per instruction:
   Press 'e' for Encryption.
   Press 'd' for Decryption.
   =====================> d
   ```

3. **Choose file input:**
   ```
   Press 't' for text.
   Press 'f' for file.
   =====================> f
   ```

4. **Enter the filename:**
   ```
   Enter Correct FileName: encrypted_file.txt
   ```

5. **Enter the shift value:**
   ```
   Enter the shift value: 3
   ```

6. **View or save the decrypted content:**
   ```
   Press v to View.
   Press s to Save.
   Press b for Both.
   ======================> v
   ```

7. **Output:**
   ```
   The decrypted content of given file are:
   -------------------------------------------------------
   Hello World
   ```

## Functions

- `welcome()`: Displays a welcome message.
- `encrypt_or_decrypt()`: Prompts the user to choose between encryption and decryption.
- `enter_message(task)`: Asks the user to choose between text input or file input.
- `process_file(file_name, task)`: Reads the content of a file.
- `write_message(encrypted_file_content)`: Writes the encrypted content to a file.
- `encrypt(normal_text, key)`: Encrypts the given text using the specified shift key.
- `decrypt(encrypted_text, key)`: Decrypts the given text using the specified shift key.
- `loop_terminator()`: Asks the user if they want to perform another operation.
- `shift_value()`: Prompts the user to enter the shift value.
- `main()`: The main function that orchestrates the program flow.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Suwan Dhital
