Python TCP/IP Client-Server Messaging
---------------------

A simple TCP/IP client-server messaging app written in Python.
This project demonstrates how to build socket-based communication with support for basic commands.

---------------------
 Features
---------------------
- TCP/IP communication using Python sockets
- Multi-client support with threading (server)
- Command-line interface
- Built-in server commands:
    - time         => returns current server time
    - echo <msg>   => replies back with your message
    - help         => shows available commands
    - quit         => disconnects the client

---------------------
 File Overview
---------------------
- server.py    : The main server application
- client.py    : A simple TCP client interface
- README.txt   : This file

---------------------
 Requirements
---------------------
- Python 3.x
- No external libraries needed

---------------------
 How to Run
---------------------
1. Open Terminal 1:
   > python server.py

2. Open Terminal 2:
   > python client.py

3. In the client, try commands like:
   > help
   > time
   > echo Hello there!
   > quit

---------------------
 Example Session
---------------------
You: help
Server: Commands:
 - time
 - echo <message>
 - help
 - quit

You: time
Server: Wed Jun 26 12:45:00 2025

You: Hello world!
Server: Hello world!

You: quit
Disconnected.

---------------------
 Customization Ideas
---------------------
- Add GUI with Tkinter or PyQt
- Use SSL/TLS for encryption
- Add user authentication
- Save message logs to a file

---------------------
 License
---------------------
This project is open-source under the MIT License.

---------------------
 Author
---------------------
Created by Evelyn Ayanwale
