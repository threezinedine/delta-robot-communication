import socket


MESSAGES = {
        b'test': b'ok',
        b'\x30\x30\x00\x00\x00\x22\x01\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00':
        b'\x30\x30\x00\x00\x00\x08\x01\x03\x00\x06\x00\x00\x00\x00'
        }


def binding_server(ip_address, port, messages=MESSAGES, default=b'fail'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((ip_address, port))
        server.listen()

        conn, addr = server.accept()
        msg = conn.recv(1000)
        if msg in messages.keys():
            conn.send(messages[msg])
        else:
            conn.send(default)

def create_a_socket_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client
