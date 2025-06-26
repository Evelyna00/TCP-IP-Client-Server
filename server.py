import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 65432


def handle_client(conn, addr):
    print(f"{addr} connected.")
    conn.sendall(b"Welcome to the Python TCP Server. Type 'help' for commands.\n")

    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data:
                break
            print(f"[{addr}] {data}")

            if data.lower() == "time":
                response = time.ctime()
            elif data.lower().startswith("echo "):
                response = data[5:]
            elif data.lower() == "help":
                response = "Commands:\n - time\n - echo <message>\n - help\n - quit"
            elif data.lower() == "quit":
                response = "Goodbye!"
                conn.sendall(response.encode())
                break
            else:
                response = "Unknown command. Type 'help' for available commands."

            conn.sendall((response + '\n').encode())
        except ConnectionResetError:
            break

    print(f"{addr} disconnected.")
    conn.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"{threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
