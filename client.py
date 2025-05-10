import socket
import time

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

def get_player_move():
    try:
        #prompt the user to enter their move. The move should be a number between 1 and 9.
        move = input("Enter your move (1-9): ").strip()   #check if the entered digit is valid 
        if move.isdigit() and 1 <= int(move) <= 9: #convert the move to an integer and return it if it's valid
            return int(move)  
        else:
            print("Invalid move. Please enter a number between 1 and 9.") #if its not valid , print error
            return None
    except Exception as e:
        print(f"Error: {e}") #if an unexpected error occurs, print the error message
        return None

def start_client():
     #create a new socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect the client to the server at the specified IP address (127.0.0.1) and port (12345)
    client.connect(("127.0.0.1", 12345))

    while True:
        #recv data from the server(up to 1024 bytes)
        data = client.recv(1024).decode()
        print(data)

        if "Your turn" in data:
            #set a timer for player's turn
            start_time = time.time()
            timeout = 10  #timeout in seconds
            move = None    #variable to store the players move 

                #start a loop that keeps checking if the player has made a move within the timeout
            while time.time() - start_time < timeout:
                move = get_player_move()
                if move is not None:
                    break

            if move is None or time.time() - start_time >= timeout:  #if moved after timeout 
                print("Time's up! You lost due to timeout.")
                client.sendall(b"Timeout")
                break

            #if the player made a valid move, send the move to the server
            client.sendall(str(move).encode())

             #recv response from the server about the result of the move
            data = client.recv(1024).decode()
            print(data)
        
        elif "Thanks for playing" in data:
            print(data)
            break

        elif "Do you want a rematch?" in data:
            rematch_response = input("Do you want a rematch? (yes/no): ").strip().lower()
             #send the player's response to the server
            client.sendall(rematch_response.encode())

    client.close()  #ater the game ends(either due to timeout or rematch response),close the client's connection

if __name__ == "__main__":
    start_client()
