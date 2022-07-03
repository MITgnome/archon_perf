# echo-client.py

import socket
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 8192

data = bytearray(2048 * 1024 * 2)


def recvall(sock, data_all):
    data_curr_ptr = 0
    while True:
        # print(".", end="\r")
        part = sock.recv(RECV_BUF_SIZE)
        data_all[data_curr_ptr:data_curr_ptr + len(part) - 1] = part
        data_curr_ptr = data_curr_ptr + len(part)
        if len(part) < RECV_BUF_SIZE:
            # either 0 or end of data
            break
    return data_all


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
    s.connect((HOST, PORT))

    s.send(b"SENDCUBE")

    ts_start = time.time()
    data = recvall(s, data)
    ts_elapsed = time.time() - ts_start
    print("\nReceive Complete")
    print(f"Time Elapsed: {ts_elapsed}")
    # print(f"Received {data!r}")
    print(f"Received {len(data)}")
    s.close()
