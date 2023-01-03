import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
# Encrypt and decrypt a file with choose function using RSA

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

def main():
    # Get the input and output file names
    input_file = input('Enter the name of the input file: ')
    output_file = input('Enter the name of the output file: ')

    # Get the user's choice
    choice = input('Encrypt or decrypt? [1/2]: ')

    # Encrypt the file
    if choice == '1':
        encrypt_file(input_file, output_file, public_key)
    # Decrypt the file
    elif choice == '2':
        decrypt_file(input_file, output_file, private_key)
    # Invalid choice
    else:
        print('Error: Invalid choice.')
        sys.exit(1)



if __name__ == '__main__':
    main()