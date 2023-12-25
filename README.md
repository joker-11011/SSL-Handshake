# SSL-Handshake
Introduction:
The SSL handshake is a critical process in establishing a secure communication channel over the internet. This code provides an overview of the SSL handshake, highlighting its key steps and the significance of each in securing online transactions and sensitive information. It makes use of two keys, public and private, in order to provide confidentiality and authenticity by securing the communication between the two users and making sure the uses knows that the other is genuine and vice versa.

Methodology:
The SSL handshake has the users generate two keys: a private key, which is present only with the users, and a public key, which as the name suggests is available publicly to everyone.

We have tried to take a different approach to the key verification process by taking a page out of Diffie-Hellman key exchange process. First the users agree on codewords for each other in order to verify their keys. These codewords can be shared indirectly. Then, the user wanting to start communicating sends a 'Hello' message to the other user for indication. Now the other user also sends 'Hello' message and they share their public keys.

Now the users encrypt the codewords to be sent using the public keys of the other using the RSA algorithm. When received, the users decrypt the encrypted codewords to get the original codeword. If the codewords are verified, the key verification is successful and the users can now start communicating by using the keys knowing that the communication is secure and authenticated.
