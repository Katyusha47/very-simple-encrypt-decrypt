# RSA File Encryption/Decryption
This script allows you to encrypt and decrypt files using the RSA algorithm. The RSA algorithm is a public-key cryptography algorithm that is widely used for secure data transmission. It is based on the difficulty of factoring large numbers.

# Features
* Generates a new RSA key pair using a 2048-bit key length
* Encrypts and decrypts files using the RSA algorithm
* Reads and processes the input file in 128-byte blocks
* Pads the output file with zeros to a multiple of the block size (256 bytes) during decryption
* Displays an error message and continues to the next block if decryption fails for a block of data

# Requirements
* Python3
* pycryptodomex
```bash
pip install pycryptodomex
```

# Usage
To run the script, use the following command:
```bash
python encrypt-decrypt.py
```
You will be prompted to enter the name of the input file, the name of the output file, and whether you want to encrypt or decrypt the file.

# Example
```bash
Enter the name of the input file: input.txt
Enter the name of the output file: output.txt
Encrypt or decrypt? [1/2]: 1
```
This will encrypt the input.txt file and save the encrypted data to output.txt.

```bash
Enter the name of the input file: input.txt
Enter the name of the output file: output.txt
Encrypt or decrypt? [1/2]: 2
```
This will decrypt the input.txt file and save the decrypted data to output.txt

# Notes
* The RSA key pair is generated using a 2048-bit key length. This key length is considered to be sufficient for most purposes and provides an acceptable level of security.
* The input file is read and processed in 128-byte blocks. This means that the input file is divided into blocks of 128 bytes, and each block is encrypted or decrypted separately.
* The output file is padded with zeros to a multiple of the block size (256 bytes) during decryption. This is necessary because the RSA algorithm requires that the input data be a multiple of the block size.
* If the decryption fails for a block of data, an error message is displayed and the script continues to the next block. This can happen if the decryption key is incorrect or if the data has been tampered with.
