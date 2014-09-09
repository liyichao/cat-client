#!/usr/bin/env python
# coding: utf-8


from cat.msg_manager import MessageManager
from cat.msg import Message
import time


class Transaction(Message):
    def __init__(self, ttype, name):
        super(Transaction, self).__init__(ttype, name)
        self.children = []
        self.manager = MessageManager()
        self.start = self.timestamp
        self.end = -1

    def add_child(self, msg):
        self.children.append(msg)

    def get_children(self):
        return self.children

    def complete(self):
        self.end = time.time()
        self.manager.end(self)

    def get_duration(self):
        return self.end - self.start

