#! /usr/bin/env python
# coding: utf-8

import socket
import struct

host = 'localhost'
port = 2280

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

msg = ''
msg += "PT1\tdomain\thostName\tipAddress\tthreadGroupName\tthreadId\tthreadName\tmessageId\tparentMessageId\trootMessageId\tsessionToken\n"

msg += "E2012-01-02 15:33:41.987\ttype\tname\t0\there is the data.\t\n"

size = struct.pack('!i', len(msg))
print size

msg = size + msg

s.sendall(msg)