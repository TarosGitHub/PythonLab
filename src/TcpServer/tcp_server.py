#! /usr/bin/env python3

"""
See Also
--------
https://docs.python.org/ja/3/library/socketserver.html
"""

import socketserver

class RequestHandler(socketserver.BaseRequestHandler):
    _BUFFER_SIZE = 1024

    def setup(self):
        print(f"Accepted. {self.client_address[0]}")

    def handle(self):
        while True:
            self.data = self.request.recv(self._BUFFER_SIZE).strip()
            print(self.data)
            if "exit" == self.data.decode("utf-8", "replace"):
                break

    def finish(self):
        print(f"Closed. {self.client_address[0]}")
        return super().finish()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    print("TCP Server start.")

    with socketserver.TCPServer((HOST, PORT), RequestHandler) as server:
        # Activate the server; this will keep running until you interrupt the program with Ctrl-C
        server.serve_forever()

    print("TCP Server has finished.")

"""
Client is like:

% python3
Python 3.11.6 (main, Oct  3 2023, 02:51:45) [Clang 14.0.3 (clang-1403.0.22.14.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import socket
>>> HOST, PORT="localhost", 9999
>>> client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> client.connect((HOST, PORT))
>>> client.sendall(bytes("hoge\n","utf-8"))
>>> client.sendall(bytes("fuga\n","utf-8"))
>>> client.sendall(bytes("exit","utf-8"))
>>> client.close()
>>> client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> client.connect((HOST, PORT))
>>> client.sendall(bytes("fuga\n","utf-8"))
>>> client.sendall(bytes("fuga\n","utf-8"))
>>> client.sendall(bytes("exit","utf-8"))
>>> client.close()
>>> exit()
"""
