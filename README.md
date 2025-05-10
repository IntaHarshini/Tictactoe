# Tictactoe
Multiplayer Tic Tac Toe game using Python sockets with two clients playing against each other. Includes rematch option, 10-second turn timer, and a server-controlled leaderboard.



# 🎮 Multiplayer Tic Tac Toe Game Using Python Sockets

This is a multiplayer Tic Tac Toe game built in Python using socket programming. The server handles client connections, pairing them together when the number of clients is even, or playing against the last unpaired client if the number is odd. The game ensures proper state management and secure communication between clients and the server.

---

## 🚀 Features

- **Socket-based multiplayer**: Clients communicate with the server to play the game.
- **Even client pairing**: When the number of clients is even, clients are paired to play against each other.
- **Server-player for odd clients**: If the number of clients is odd, the last unpaired client plays against the server.
- **Unique symbols**: Each player receives a distinct symbol (X or O) for gameplay.
- **Game state management**: The game ensures the state is properly updated and displayed during play.
- **Real-time game display**: The game board is displayed in the terminal with each move.
- **Client-Server communication**: Uses sockets to manage communication between multiple clients and the server.

---

## 🧠 Technologies Used

| Component         | Tool/Library                   |
|-------------------|---------------------------------|
| Programming       | Python 3                        |
| Networking        | socket                          |
| Multithreading    | threading                       |

---

## 🖥️ How to Run This Project on Your Machine

### 📋 Prerequisites

Make sure you have Python 3 installed.
Make sure that all the server and both the clients are under same network.

### 🛠️ Steps to Run the Server and Client

step1:
Run the server code
```bash
 server.py
and then enter the names of the play

step2:
 open the client.py and update this line with your server's IP and Run the client
```bash
host = "xxx.xxx.xxx.xxx" #change this to your server's IP and Run the client
Open two separate terminals and then
```bash
client.py

step3:
Now start playing the game 
Move within 10seconds

step4:
choose for the rematch option(if required)







