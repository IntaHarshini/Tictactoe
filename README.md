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
