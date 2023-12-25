from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

#Code word exchange
print("Codewords exchanged between client and server for key exchange process:")
cw1 = b"cat"
cw2 = b"dog"
print("Client's codeword for server: ", cw1)
print("Server's codeword for client: ", cw2)

#Initiate coversation via 'Hello' message
client_message= input("\nTo initiate conversation, Enter 'Hello':")
if client_message == "Hello" :
    print("Server: Hello! \n Lets verify our keys before sending messages")

    #Key generation
    c_private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    c_public_key = c_private_key.public_key()
    print("\nClient's private key: ", c_private_key)
    print("Client's public key: ", c_public_key)

    s_private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    s_public_key = s_private_key.public_key()
    print("Server's private key: ", c_private_key)
    print("Server's public key: ", c_public_key)

    # Key conformation process

    # Client encrypting codeword using server's public key
    c_cip1 = s_public_key.encrypt(
        cw1,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    print("\n\nCipherword from client after encryption using server's public key: ", c_cip1)

    # Server encrypting codeword using client's public key
    s_cip2 = c_public_key.encrypt(
        cw2,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    print("Cipherword from server after encryption using client's public key: ", s_cip2)

    # Server decrypting the cipherword using its private key
    s_cw11 = s_private_key.decrypt(
        c_cip1,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    print("\n\nServer's decrypted codeword: ", s_cw11)

    # Client decrypting the cipherword using its private key
    c_cw22 = c_private_key.decrypt(
        s_cip2,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    print("Client's decrypted codeword: ", c_cw22)

    #Verification
    if s_cw11 == cw1 and c_cw22 == cw2:
        print("\n\nKey verification successful")

    #Message transfer
    print("Since key verification is successful, Client and server can now start exchanging messages using the keys.")
    print("For Example, if the server wants to send a message:\n")
    message = b"Mac and Cheese:"

    print("Server's message: ", message)
    ciphertext = c_public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    print("The message sent by server after encryption using the clients public key: ", ciphertext)

    plaintext = c_private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )

    print("The message decrypted by the client using its private key: ", plaintext)
else:
    print("Invalid")
