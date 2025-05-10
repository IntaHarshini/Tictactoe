import socket
import threading  #Handle multiple players without blocking the main thread.
import json       #Store and load leaderboard data.
import os         #Check if a file exists.
import time       #Track time for timeouts.

BOARD_POSITIONS = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
}

def print_board(board):
    display = ""
    count = 1
    for row in board:
        row_display = []
        for cell in row:
            if cell == ' ':
                row_display.append(str(count))
            else:
                row_display.append(cell)
            count += 1
        display += f" {row_display[0]} | {row_display[1]} | {row_display[2]} \n"
        if count <= 9:
            display += "---+---+---\n"
    return display

def check_winner(board, mark):
         #row match
    for row in board:
        if all(cell == mark for cell in row):
            return True
        #col match 
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
        #check both diagnols 
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def load_leaderboard():
    if os.path.exists("leaderboard.json"):       #check if the file exits 
        with open("leaderboard.json", "r") as f:   #Read and parse the JSON content into a Python dictionary and return it
            return json.load(f)
    return {}    #if doesnt exist then return empty dic 

def save_leaderboard(leaderboard):
    with open("leaderboard.json", "w") as f:
        json.dump(leaderboard, f, indent=2)

def update_leaderboard(leaderboard, winner, player1, player2):
    for player in [player1, player2]:
        if player not in leaderboard:    #if not in the leadboard dic then initialize 
            leaderboard[player] = {'wins': 0, 'losses': 0, 'ties': 0}

    if winner == "tie":      #if its a tie then both are incremented to 1 
        leaderboard[player1]['ties'] += 1
        leaderboard[player2]['ties'] += 1
    else:
        leaderboard[winner]['wins'] += 1
        loser = player2 if winner == player1 else player1
        leaderboard[loser]['losses'] += 1

def prompt_rematch(client1, client2):
    try:
        client1.sendall(b"Do you want a rematch? (yes/no): ")
        client2.sendall(b"Do you want a rematch? (yes/no): ")
        resp1 = client1.recv(1024).decode().strip().lower()   #recv response from client1 upto 1024 bytes 
                            #decode the response from bytes to string  
                            # strip any leading/trailing whitespace, and convert to lowercase.
        resp2 = client2.recv(1024).decode().strip().lower()
        return resp1 == "yes" and resp2 == "yes"     #both should reply yes 
    except:
        return False

def handle_client(client1, client2, player1_name, player2_name):
    leaderboard = load_leaderboard()

    while True:
        board = [[" "]*3 for _ in range(3)]
        current = client1
        other = client2
        current_mark = "X"
        other_mark = "O"
        current_name = player1_name
        other_name = player2_name

        while True:
            board_str = print_board(board)  #disply the current board to both the player
            #send the current board and prompt player1 for their move
            current.sendall(f"\n{board_str}\nYour turn ({current_mark}). Enter a number (1-9): ".encode())
            other.sendall(f"\n{board_str}\nWaiting for {current_name} to move...".encode())
                #Set a timeout of 10 seconds for making a move
            start_time = time.time()
            timeout = 10  # Timeout in seconds
            move = None  #variable to store the move 

        # Wait for a move from the current player within the timeout period
            while time.time() - start_time < timeout:
                move = current.recv(1024).decode().strip()
                if move.isdigit() and int(move) in BOARD_POSITIONS:    #check if it in valid range and convert into board co-ordinates 
                    row, col = BOARD_POSITIONS[int(move)]
                    if board[row][col] == " ":
                        board[row][col] = current_mark
                        break    #exit the move loop 
                    else:
                           # If the cell is already taken, ask the player to try again
                        current.sendall("That cell is already taken. Try again.\n".encode())
                else:
                     # If the move is invalid (not a number or out of range), ask the player to try again
                    current.sendall("Invalid move. Please enter a number from 1 to 9.\n".encode())
            #If no valid move was made or timeout occurred
            if move is None or time.time() - start_time >= timeout:  ## Inform both players about the timeout
                current.sendall(f"\nTime's up! You lost because you didn't make your move in time.\n".encode())
                other.sendall(f"\n{current_name} lost due to timeout.\n".encode())
                update_leaderboard(leaderboard, other_name, player1_name, player2_name) ## Update the leaderboard to reflect the loss due to timeout
                break   #exit the game loop(round is over due to timeout)

            if check_winner(board, current_mark):    #check if current player has won the game 
                board_str = print_board(board)  #get the updated leader bopard 
                current.sendall(f"\n{board_str}\nYou win!\n".encode())  #inform the player abt victory and loss
                other.sendall(f"\n{board_str}\nYou lose. {current_name} won.\n".encode())
                update_leaderboard(leaderboard, current_name, player1_name, player2_name)
                break #exit game (round is over with a winner )
                    # check if the board is full (tie game)
            if board_full(board):
                board_str = print_board(board)  #get leadboard
                current.sendall(f"\n{board_str}\nIt's a tie!\n".encode())  #inform the players abt tie 
                other.sendall(f"\n{board_str}\nIt's a tie!\n".encode())
                update_leaderboard(leaderboard, "tie", player1_name, player2_name)
                break  #exit the game 

             #Swap turns between the players (current player becomes the other player)
            current, other = other, current
            current_mark, other_mark = other_mark, current_mark
            current_name, other_name = other_name, current_name

        save_leaderboard(leaderboard)  #Save the updated leaderboard to the file

        if not prompt_rematch(client1, client2):  #Prompt both players for a rematch
            client1.sendall(b"Thanks for playing! Goodbye.\n")  ##If either player does not want a rematch, send a farewell message
            client2.sendall(b"Thanks for playing! Goodbye.\n")
            break
 # Close the connections for both players
    client1.close()
    client2.close()

def start_server():
    #Create a new socket object for the server using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     #Bind the server socket to IP address "127.0.0.1" (localhost) and port 12345
    server.bind(("127.0.0.1", 12345))
     #Tell the server to start listening for incoming connections, with a maximum of 2 clients in the waiting queue
    server.listen(2)
    print("Server started, waiting for players...")

            #get the names of both the players 
    player1_name = input("Enter Player 1's name (X): ").strip()
    player2_name = input("Enter Player 2's name (O): ").strip()

    client1, addr1 = server.accept()   #Send a welcome message to Player 1
    print(f"Player X connected from {addr1}")
    client1.sendall(f"Welcome {player1_name}! You are X.\nWaiting for another player...\n".encode())

    client2, addr2 = server.accept()  #Wait for Player 2 to connect to the server
    print(f"Player O connected from {addr2}")
    client2.sendall(f"Welcome {player2_name}! You are O.\nGame starting...\n".encode())
    client1.sendall("Game starting...\n".encode())  # Inform Player 1 that the game is starting now

    #Start a new thread to handle the game logic between the two players. 
    #The `handle_client` function is called in a new thread with the clients and their names.

    threading.Thread(target=handle_client, args=(client1, client2, player1_name, player2_name)).start()

if __name__ == "__main__":
    start_server()
