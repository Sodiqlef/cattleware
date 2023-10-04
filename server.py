import socket

# Define the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to a specific host and port
host = '127.0.0.1'  # Loopback address for local testing
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(2)  # Allow up to 2 players

# Function to display the Tic-Tac-Toe board


def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Function to check if a player has won


def check_winner(symbol):
    # Check rows, columns, and diagonals for a win
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == symbol:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == symbol:
            return True
    if board[0] == board[4] == board[8] == symbol or board[2] == board[4] == board[6] == symbol:
        return True
    return False

# Function to reset the game board


def reset_board():
    global board
    board = [' ' for _ in range(9)]


print("Server is waiting for players to connect...")

# Accept the first player
player1_socket, player1_address = server_socket.accept()
player1_socket.send("You are Player 1 (X).".encode())

# Accept the second player
player2_socket, player2_address = server_socket.accept()
player2_socket.send("You are Player 2 (O).".encode())

print("Both players are connected and the game is starting!")


while True:
    reset_board()
    current_player = player1_socket

    while True:
        display_board()
        current_player.send("Your move (1-9): ".encode())
        move = current_player.recv(1024).decode()

        if not move:
            break

        if not move.isdigit() or not (1 <= int(move) <= 9) or board[int(move) - 1] != ' ':
            current_player.send("Invalid move. Try again.".encode())
        else:
            board[int(move) - 1] = 'X' if current_player == player1_socket else 'O'
            current_player = player2_socket if current_player == player1_socket else player1_socket

        # Check for a win or tie
        if check_winner('X'):
            display_board()
            player1_socket.send("You win!\n".encode())
            player2_socket.send("Player 1 wins!\n".encode())
            break
        elif check_winner('O'):
            display_board()
            player2_socket.send("You win!\n".encode())
            player1_socket.send("Player 2 wins!\n".encode())
            break
        elif ' ' not in board:
            display_board()
            player1_socket.send("It's a tie!\n".encode())
            player2_socket.send("It's a tie!\n".encode())
            break

    # Close the sockets
    player1_socket.close()
    player2_socket.close()
    server_socket.close()
