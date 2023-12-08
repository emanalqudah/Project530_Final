# Project530

# Network Security Python based Project :
# Data Encryption to prevent Packet Sniffing Attack



Welcome to my Data Encryption to prevent Packet Sniffing Attack Python project!
This project will  eventually show how Encryption for sensitive Data such as passowords prevent Packet Sniffing Attack.
This code introduces Client- Server  model implementation in python.My Implementation assumes that there is a maximum number of  clients can connect to the server .
This code does not implement any kind of security measures to prevent attacks against the login system.
The basic outline of my implementation for the communication module  in Python is :

Open VSCode :
1. Run the server.py file . 
2. Run multiple instance of client.py file 
3. Upon sending data from each client ,the server will recieve the data prompted each client to send data more and more .
4. 4. Open Wireshark to see that you can sniff the sent data 



To send encrypted data ,open new VSCode :

1. Run the En_server.py file . 
2. Run multiple instance of En_client.py file 
3. Upon sending data from each client ,the server will recieve the encrypted data prompted each client to send data more and more .
4. Open Wireshark to see that you cannot sniff the encrypted sent data


## Installation

To use this project, follow these steps:

1. Install Python ,VSCode and Wireshark (see README) 
2. Clone the repository to your local machine:

      git clone https://github.com/emanalqudah/Project530_Final


3. Open the project files using VSCode .
4. Use cmd->pip install <Modulename> to install any Module not installed with Python on your machine .
5.use cmd ->python server.py to run the server file
6.5.use cmd ->python client.py to run the client file
