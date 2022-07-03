# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

image_cube = bytearray(2048 * 1024 * 2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    # Get the size of the socket's send buffer
    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Send Buffer size [Before]:%d" % bufsize)
    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Receive Buffer size [Before]:%d" % bufsize)

    # Set the socket's Send and Receive Buffers
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Send buffer size [After]:%d" % bufsize)
    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Receive buffer size [After]:%d" % bufsize)

    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(RECV_BUF_SIZE)
            print(f"Received from Client {data}")
            if data == b"SENDCUBE":
                print("Sending ImageCube")
                conn.sendall(image_cube)
                print("Done Sending ImageCube")
                conn.close()
                print("Connection Closed")
                break
        print("Done with conn")
        print("Set socket reuseaddr and close socket")
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.close()
