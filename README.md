# 🎮 Multiplayer Tic Tac Toe Using Python Sockets

Multiplayer Tic Tac Toe game using Python sockets with two clients playing against each other. Includes rematch option, 10-second turn timer, and a server-controlled leaderboard.

---

## 🚀 Features

- Real-time multiplayer Tic Tac Toe  
- 10-second timeout per move (enforced automatically)  
- Win, loss, or tie detection  
- Option for rematch after each game  
- Leaderboard tracking wins, losses, and ties  
- Supports multiplayer across different machines (on the same network)  
- Graceful handling of disconnects  

---

## 🧠 Technologies Used

| Component       | Tool/Library         |
|----------------|----------------------|
| Programming     | Python 3             |
| Networking      | `socket`             |
| Threading       | `threading`          |
| Data Storage    | `json` (for leaderboard) |
| Timeout Control | `time`               |

---

## 🖥️ How to Run This Project

### 📋 Prerequisites

Make sure Python 3 is installed on all machines, and the following files are in the same directory:

- `server.py`
- `client.py`

---

### ✅ Step-by-Step Instructions

#### 1. Start the Server

On one terminal or machine (host/server):

```bash
python3 server.py


You'll be asked to enter player names for Player X and Player O. The server will then wait for two clients to connect.

2. Start the Clients
On two different terminals or machines (clients):

```bash
python3 client.py
Clients will automatically connect and be paired for a game.

3. Play the Game
Players take turns by entering positions (1–9).
Each player has 10 seconds to make a move.
The server announces the winner or tie.
After each game, players are prompted for a rematch.

🌐 Network Requirements
All devices must be on the same local network.
Server IP 127.0.0.1 is for local testing.
For LAN play, replace it with the host machine's IP address in both server.py and client.py.

📂 Files Overview
server.py – Manages connections, gameplay, validation, and leaderboard.
client.py – Connects to server, handles user input/output.
leaderboard.json – Auto-generated file storing win/loss/tie records persistently.

🏁 Conclusion
This project demonstrates:
Socket-based multiplayer game logic
Real-time client-server communication
Multithreaded server handling for concurrent gameplay
Timeout enforcement and fair-play features

---

✅ **Copy-paste the entire code above into your `README.md` file**, and it will render perfectly.

Would you like me to generate a `.md` file you can download directly?


