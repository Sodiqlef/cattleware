import threading
import socket

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'  # Loopback address for local testing
port = 12345
client_socket.connect((host, port))

# Function to display the Tic-Tac-Toe board


def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Function to receive and display messages from the server


def receive_and_display():
    while True:
        message = client_socket.recv(1024).decode()
        print(message)


# Start a thread to receive and display messages
receive_thread = threading.Thread(target=receive_and_display)
receive_thread.start()

while True:
    try:
        move = input("Enter your move (1-9): ")
        client_socket.send(move.encode())
    except KeyboardInterrupt:
        break

# Close the client socket
client_socket.close()
