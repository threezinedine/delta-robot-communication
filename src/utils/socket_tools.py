import socket


def binding_server(ip_address, port, messages, default=b'fail'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((ip_address, port))
        server.listen()

        conn, addr = server.accept()
        msg = conn.recv(1000)
        print(msg, messages)
        if msg.decode() in messages.keys():
            conn.send(messages[msg.decode()].encode())
        else:
            conn.send(default)

def create_a_socket_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client
