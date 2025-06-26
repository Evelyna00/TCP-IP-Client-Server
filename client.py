import socket

HOST = '127.0.0.1'  # local host
PORT = 65432


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(s.recv(1024).decode())  # Welcome message

        while True:
            msg = input("[ENTER MESSAGE HERE]")
            if msg.strip().lower() == "quit":
                s.sendall(b"quit")
                print("Disconnected.")
                break
            s.sendall(msg.encode())
            response = s.recv(1024).decode()
            print(f"Server: {response.strip()}")


if __name__ == "__main__":
    start_client()
