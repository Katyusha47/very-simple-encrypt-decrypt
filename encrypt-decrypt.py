from Crypto import *
from Crypto.PublicKey import RSA
from Crypto.Util import *
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

# Generate a new RSA key pair
key = RSA.generate(2048)

# Extract the public and private key
public_key = key.publickey()
private_key = key

# Function to encrypt a file using RSA
def encrypt_file(input_file, output_file, public_key):
    # Open the input and output files
    with open(input_file, 'rb') as fin, open(output_file, 'wb') as fout:
        # Create a new RSA cipher
        cipher = PKCS1_OAEP.new(public_key)

        # Read the input file one block at a time
        while True:
            # Read the next block of data
            data = fin.read(128)

            # If we have reached the end of the file, break out of the loop
            if not data:
                break

            # Encrypt the data and write it to the output file
            fout.write(cipher.encrypt(data))

# Function to decrypt a file using RSA
def decrypt_file(input_file, output_file, private_key):
    # Open the input and output files
    with open(input_file, 'rb') as fin, open(output_file, 'wb') as fout:
        # Create a new RSA cipher
        cipher = PKCS1_OAEP.new(private_key)

        # Read the input file one block at a time
        while True:
            # Read the next block of data
            data = fin.read(256)

            # If we have reached the end of the file, break out of the loop
            if not data:
                break

            # Pad the data with zeros if it is not a multiple of the block size
            data = data.ljust(256, b'\0')

            # Attempt to decrypt the data
            try:
                decrypted_data = cipher.decrypt(data)
            except ValueError:
                # If the decryption fails, display an error message and continue to the next block of data
                print('Error: Decryption failed.')
                continue

            # Write the decrypted data to the output file
            fout.write(decrypted_data)

# Test the encryption and decryption functions
input_file = input('Input your filename: ')
encrypted_file = input('Input output filename for save the encrypted: ')
decrypted_file = input('Input output filename for save the decrypted: ')


# Encrypt the input file
encrypt_file(input_file, encrypted_file, public_key)


# Decrypt the encrypted file
decrypt_file(encrypted_file, decrypted_file, private_key)


# Check if the decrypted file is the same as the input file
with open(input_file, 'rb') as fin, open(decrypted_file, 'rb') as fout:
    if fin.read() == fout.read():
        print('Success: The decrypted file is the same as the input file.')
    else:
        print('Error: The decrypted file is not the same as the input file.')
