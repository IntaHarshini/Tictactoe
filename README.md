# 🎮 Multiplayer Tic Tac Toe Using Python Sockets

A real-time, socket-based multiplayer Tic Tac Toe game where two clients connect and play against each other. The game features a 10-second turn timer, rematch option, and a server-maintained leaderboard.

---

## 🚀 Features

- ✅ Real-time multiplayer gameplay  
- ⏱️ 10-second timeout per move (auto-forfeit on timeout)  
- 🏆 Win, loss, or tie detection  
- 🔁 Option for rematch after each game  
- 📊 Leaderboard tracking wins, losses, and ties  
- 🌐 LAN support: play across different machines on the same network  
- 📤 Graceful handling of player disconnects  

---

## 🧠 Technologies Used

| Component        | Tool/Library         |
|------------------|----------------------|
| Programming      | Python 3             |
| Networking       | `socket`             |
| Threading        | `threading`          |
| Timeout Control  | `time`               |
| Data Storage     | `json`               |

---

## 🖥️ How to Run This Project

### 📋 Prerequisites

- Python 3 must be installed on all participating machines.
- Ensure the following files are in the same directory:
  - `server.py`
  - `client.py`

---

### ✅ Step-by-Step Instructions

#### ▶️ Start the Server

On the host machine:

```bash
python3 server.py
```

- Enter names for Player X and Player O when prompted.
- The server will wait for two clients to connect.

---

#### 🧑‍🤝‍🧑 Start the Clients

On **two different terminals** or **machines**:

```bash
python3 client.py
```

- Clients will automatically connect and be paired to play.

---

#### 🎮 Play the Game

- Players take turns entering positions (1–9) on the grid.
- Each player has **10 seconds** to make a move.
- The server announces the game result: win, tie, or timeout.
- After the game, players are asked if they want a rematch.
- Leaderboard updates after each match.

---

## 🌐 Network Requirements

- All devices must be on the **same local network**.
- `127.0.0.1` is used for local testing.
- For LAN play, replace `127.0.0.1` in both `server.py` and `client.py` with the host machine’s actual **IP address** (e.g., `192.168.1.5`).

---

## 📂 Files Overview

| File               | Description                                                              |
|--------------------|--------------------------------------------------------------------------|
| `server.py`        | Manages connections, turn-taking, validation, timeout, rematches, leaderboard. |
| `client.py`        | Handles user input/output and communication with the server.             |
| `leaderboard.json` | Auto-created by the server to store persistent win/loss/tie records.     |

---

## 🏁 Conclusion

This project demonstrates:

- 🧠 Socket-based multiplayer game design  
- ⚡ Real-time client-server communication  
- 🔄 Multi-threaded server handling for concurrency  
- ⏱️ Timeout enforcement for fair play  
- 🗃️ Persistent leaderboard using JSON  

---

