from termcolor import colored
from Crypto.Cipher import AES as AESCipher
import socket
import sys
import os
import hashlib


# Receiving The Value Of IP and PORT From the User
LISN_IP = input(colored("Enter The Local IP of your Machine: ", "green"))
LISN_PORT = int(input(colored("Enter The port no. to bind: ", "green")))
USER_NAME = input(colored("Please Choose a Username for Chat: "))

os.system('clear')
print(colored("<1>ONLINE...", "green", attrs=['reverse', 'blink']))

name = USER_NAME + ">> "
encoded_name = name.encode()

# this chat function starts the server


def chat():
    s = socket.socket()
    s.bind((LISN_IP, LISN_PORT))
    s.listen(1)
    conn, addr = s.accept()
    print(colored(f"[+] {addr} Connected", "green"))

    # Define key and iv here
    key = b'AB12CD34EHNS784HJLU397ERD45GY76D'
    iv = b'Cats are cute123'

    # Separate cipher objects for encryption and decryption
    encryption_cipher = AESCipher.new(key, AESCipher.MODE_CFB, iv)
    decryption_cipher = AESCipher.new(key, AESCipher.MODE_CFB, iv)

    while True:
        msg = input(colored("\nSEND-> ", "red", attrs=['bold']))
        if msg == 'bye':
            conn.send('bye'.encode())
            os.system('clear')
            print(colored("<0>OFFLINE", "red", attrs=['bold']))
            conn.close()
            sys.exit()
            break
        else:
            data = encoded_name + msg.encode()
            data_send = encryption_cipher.encrypt(data)
            conn.send(data_send)
            hash_object = hashlib.sha256(msg.encode())
            hash_value = hash_object.hexdigest()
            print(f"Hash value of message: {hash_value}")
            In_msg = conn.recv(8192)
            recv_data_enc = decryption_cipher.decrypt(In_msg)
            recv_data_unenc = recv_data_enc.decode()
            print("\n" + recv_data_unenc)

# Final Main function to run the Chat Program!


def main():
    chat()


if __name__ == "__main__":
    main()
