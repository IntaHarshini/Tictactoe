# Tictactoe
Multiplayer Tic Tac Toe game using Python sockets with two clients playing against each other. Includes rematch option, 10-second turn timer, and a server-controlled leaderboard.



# 🕹️ Multiplayer Tic Tac Toe using Python Sockets

A terminal-based, real-time multiplayer Tic Tac Toe game where two clients connect to a server. Includes a leaderboard, rematch option, and move timeout.

## 📌 Features

- Two-player multiplayer over TCP
- 10-second timeout per move
- Rematch option after each game
- Persistent leaderboard (wins, losses, ties)
- Turn-based game logic
- Text-based terminal interface

## 🛠 Requirements

- Python 3.x installed
- All files in the same directory

## 🚀 How to Run

### 1. Start the Server
```bash
python3 server.py


Enter names for both players when prompted.

2. Start the Clients
In two different terminals:

bash
Copy
Edit
python3 client.py
The game will begin automatically when two players join.

📁 Project Structure
server.py – Handles gameplay, timing, rematches, leaderboard

client.py – User interface and interaction

leaderboard.json – Stores scores

README.md – Documentation

🧰 Technologies Used
Python 3

socket – For networking

threading – For handling multiple clients

time – For timeout logic

json – For leaderboard

👤 Author
Harshini Inta


