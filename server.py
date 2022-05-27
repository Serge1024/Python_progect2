import socket
import threading

def smth_work(conn):
    data = conn.recv(8192)


users = dict()
schet = 0
sock = socket.socket()
sock.bind(('', 9090))
while True:
    conn, addr = sock.listen(1)
    users[schet] = conn
    conn.send(str(schet))
    schet += 1
