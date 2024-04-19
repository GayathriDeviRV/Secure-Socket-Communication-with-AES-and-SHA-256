from termcolor import colored
from Crypto.Cipher import AES as AESCipher
import socket
import os
import hashlib


# Receiving The Value Of IP and PORT From the User
SERVER_IP = input(colored("What Is Ip of the server running: ", "green"))
SERVER_PORT = int(
    input(colored("Enter Port No on which the server is running: ", "green")))
USER_NAME = input(colored("Please Choose a Username for Chat: "))

os.system('clear')
print(colored("<1>ONLINE..", "green", attrs=['reverse', 'blink']))

name = USER_NAME + ">> "
encoded_name = name.encode()

# chat Function Initiates the Connection to the Server


def chat():
    s = socket.socket()
    s.connect((str(SERVER_IP), SERVER_PORT))

    # Define key and iv here
    key = b'AB12CD34EHNS784HJLU397ERD45GY76D'
    iv = b'Cats are cute123'

    # Separate cipher objects for encryption and decryption
    encryption_cipher = AESCipher.new(key, AESCipher.MODE_CFB, iv)
    decryption_cipher = AESCipher.new(key, AESCipher.MODE_CFB, iv)

    while True:
        In_msg = s.recv(8192)
        recv_data_1 = decryption_cipher.decrypt(In_msg)

        # Handle decoding errors by treating data as binary
        try:
            recv_data_unenc = recv_data_1.decode('utf-8')
        except UnicodeDecodeError:
            recv_data_unenc = recv_data_1  # Treat as binary data

        hash_object = hashlib.sha256(recv_data_unenc.encode())
        hash_value = hash_object.hexdigest()
        print(f"Hash value of message: {hash_value}")

        if recv_data_unenc.strip() == 'bye':
            s.send('bye'.encode())
            os.system('clear')
            print(colored("<0>OFFLINE", "red", attrs=['bold']))
            s.close()
            break

        print("\n" + recv_data_unenc)

        Out_msg = input(colored("\nSEND-> ", "red", attrs=['bold']))

        if Out_msg == 'bye':
            s.send(Out_msg.encode())
            os.system('clear')
            print(colored("<0>OFFLINE", "red", attrs=['bold']))
            s.close()
            break
        else:
            data = encoded_name + Out_msg.encode()
            send_data = encryption_cipher.encrypt(data)
            s.send(send_data)

# Final Main function to run the Chat Program!


def main():
    chat()


if __name__ == "__main__":
    main()
