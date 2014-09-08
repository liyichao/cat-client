#!/usr/bin/env python
# coding: utf-8


from message_manager import MessageManager


class Transaction(object):
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.children = []
        self.manager = MessageManager()

    def add_child(self, msg):
        self.children.append(msg)

    def complete(self):
        self.manager.end(self)
