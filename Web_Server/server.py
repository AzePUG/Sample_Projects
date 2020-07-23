import socket


def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Tell that port 9000 will receive the requests.
        server_socket.bind(('localhost', 9000))
        # it will listen for incoming requests. For not denying subsequent calls.
        server_socket.listen(5)
        while True:
            # The blocking action - accept.
            # the next line will be executed only and only if something will be accepted.
            # it will wait forever.
            (client_socket, address) = server_socket.accept()
            # HTTP protocol says that client should talk first and that's why we are receiving from server.
            rd = client_socket.recv(5000).decode()
            pieces = rd.split("\n")
            if pieces:
                # just printing
                print(pieces[0])
            # Sending data to server
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            # Encode it before sending
            client_socket.sendall(data.encode())
            # As soon as we sent the data it is required that is should be closed
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as err:
        print("Error:\n")
        print(err)
    finally:
        server_socket.close()


if __name__ == "__main__":
    print("Access http://localhost:9000")
    create_server()