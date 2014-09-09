#!/usr/bin/env python
# coding: utf-8

from cat.msg_codec import PlainTextMsgCodec
import socket


class MsgSender(object):
    def __init__(self, host='localhost', port=2280):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.codec = PlainTextMsgCodec()

    def send(self, msg_tree):
        msg = self.codec.encode(msg_tree)
        self.socket.sendall(msg)

