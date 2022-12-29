from Crypto import *
from Crypto.PublicKey import RSA
from Crypto.Util import *
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import pickle

# Generate a new RSA key pair
secret_code = "Unguessable"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC")

file_out = open("rsa_key.bin", "wb")
file_out.write(encrypted_key)
file_out.close()

#print(key.publickey().export_key())

secret_code = "Unguessable"
encoded_key = open("rsa_key.bin", "rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)

#print(key.publickey().export_key())

# Extract the public and private key
public_key = key.publickey().export_key()
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()


private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

recipient_key = RSA.import_key(open("receiver.pem").read())
session_key = get_random_bytes(16)

private_key = RSA.import_key(open("private.pem").read())


# Function to encrypt a file using RSA
def encrypt_file(input_file, output_file, public_key):
    # Open the input and output files
    with open(input_file, 'rb') as fin, open(output_file, 'wb') as fout:
        # Create a new RSA cipher
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        data = fin.read(128)
        # Read the input file one block at a time
        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        
            
        

            
        # Encrypt the data and write it to the output file
        fout.write(cipher_rsa.encrypt(data))

# Function to decrypt a file using RSA
def decrypt_file(input_file, output_file, private_key):
    # Open the input and output files
    
    with open(input_file, 'rb') as fin, open(output_file, 'wb') as fout:
        # Create a new RSA cipher
        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        

        data = fin.read(128)
        # Decrypt the data with the AES session key
        cipher_aes = AES.new(enc_session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)        # Read the input file one block at a time
        

            
        # Decrypt the data and write it to the output file
        fout.write(cipher_rsa.decrypt(data))


# Prompt the user to choose whether to encrypt or decrypt a file
choice = input("Choose your option (1. encrypt 2. decrypt) \n")

#while choice != '3':
#    print("Please select your option: ")
#    print("1. Ecrypt")
#    print("2. Decrypt")
#    print("3. Quit")

#    choice = input()
#    match choice:
#        case '1' | '2':
#            input_file = input("Enter the input file: \n")
#            output_file = input("Enter the output file: \n")

#        case '1':
#            # Encrypt the input file and save the encrypted version to the output file
#            encrypt_file(input_file, output_file, public_key)

#        case '2':
#            # Decrypt the input file and save the decrypted version to the output file
#            decrypt_file(input_file, output_file, private_key)



if choice == '1':
    # Get the input and output filenames
    input_file = input('Enter the input file name: ')
    output_file = input('Enter the output file name: ')

    # Encrypt the input file and save the encrypted version to the output file
    encrypt_file(input_file, output_file, recipient_key)
    
    file_out.close()

elif choice == '2':
    # Get the input and output filenames
    input_file = input('Enter the input file name: ')
#
    output_file = input('Enter the output file name: ')

    # Decrypt the input file and save the decrypted version to the output file
    enc_session_key, nonce, tag, ciphertext = \
   [ file_out.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

    decrypt_file(input_file, output_file, private_key)
    file_out.close()

else:
    print('Invalid choice.')
