import os
import shutil
import logging
from cryptography.fernet import Fernet

def read_key_from_file(key_file_path):
    """
    Read the encryption key from the file.
    """
    with open(key_file_path, 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_data(file_path, key):
    """
    Encrypt the data in the file using the provided key.
    """
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def shred_file(file_path):
    """
    Overwrite the file with random data to securely delete its contents.
    """
    file_size = os.path.getsize(file_path)
    with open(file_path, 'wb') as file:
        file.write(os.urandom(file_size))

def delete_file(file_path):
    """
    Delete the file from the system.
    """
    os.remove(file_path)

def handle_nmap_script():
    """
    Handle the Nmap script.
    """
    print("Nmap script detected!")
    # Add your code here to handle the Nmap script

def handle_passphrase():
    """
    Handle the passphrase.
    """
    print("Passphrase detected!")
    # Add your code here to handle the passphrase

def encrypt_and_shred_self(file_path, cipher):
    """
    Encrypt and shred the script itself.
    """
    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

    file_size = os.path.getsize(file_path)
    with open(file_path, 'wb') as file:
        file.write(os.urandom(file_size))

    new_file_path = file_path + '.shredded'
    shutil.move(file_path, new_file_path)

def main():
    # File path and key file path
    file_path = '/workspaces/API/app.py'
    key_file_path = '/workspaces/API/encryption_key.txt'

    # Read the encryption key from the file
    encryption_key = read_key_from_file(key_file_path)

    # Create a Fernet cipher object with the key
    cipher = Fernet(encryption_key)

    # Continuously monitor for input
    while True:
        user_input = input("Enter Nmap script or passphrase: ")

        if user_input == "nmap_script":
            encrypt_and_shred_self(file_path, cipher)

            with open(key_file_path, 'rb') as key_file:
                key = key_file.read()
            encrypted_key = cipher.encrypt(key)
            with open(key_file_path, 'wb') as key_file:
                key_file.write(encrypted_key)

            shred_file(key_file_path)
            delete_file(key_file_path)

            handle_nmap_script()

        elif user_input == "passphrase":
            handle_passphrase()

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
