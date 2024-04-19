# Secure-Socket-Communication-with-AES-and-SHA-256
## Introduction
This project implements a simple client-server chat application with secure communication using AES encryption and SHA-256 hashing. The communication between the client and server is encrypted to ensure confidentiality, and message integrity is verified using SHA-256 hashing.

## Features
- Secure socket communication between client and server.
- AES encryption for message confidentiality.
- SHA-256 hashing for message integrity verification.
- Simple command-line interface for sending and receiving messages.

## Usage
### Start the server:
- python server.py
### Start the client:
- python client.py

Follow the prompts to enter the IP address, port number, and username for the chat.
Once connected, you can start sending and receiving messages securely.

## Security Considerations
Ensure that the AES encryption key and initialization vector (IV) are kept secret and securely exchanged between the client and server.
Implement proper key management practices to protect against key compromise.
Periodically update encryption keys to enhance security.
