# Trying to make very simple web browser here.
# We aim that everybody can understand this before asking the world.
import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(("data.pr4e.org", 80))
# According to he protocol
# First there should be request "type" - currently GET
# Followed by space, then URL
# Followed by protocol HTTP/1.0
# And then hit "enter" twice \r\n [headers should go here] \r\n - but we have no headers.
# Then we have to use encode() because we want it to be encoded in UTF8
cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
# Why we send here? Because we are the browser and we need to talk first.
my_sock.send(cmd)

while True:
    # Receiving from socket up to 512 characters
    data = my_sock.recv(512)
    if len(data) < 1:
        break
    # Decoding because we need to UTF8 to Unicode
    print(data.decode(), end="")

my_sock.close()
