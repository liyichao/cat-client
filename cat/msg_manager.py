#!/usr/bin/env python
# coding: utf-8

import copy
from cat.msg_id_factory import MsgIdFactory
from cat.msg_tree import MsgTree
from cat.msg_sender import MsgSender


class MessageManager(object):
    def __init__(self):
        self.context = Context()
        self.sender = MsgSender()

    def end(self, transaction):
        if self.context.end(self, transaction):
            self.context = Context()

    def start(self, transaction):
        self.context.start(transaction)

    def flush(self, msg_tree):
        self.sender.send(msg_tree)


class Context(object):
    def __init__(self):
        self.factory = MsgIdFactory()
        self.tree = MsgTree()
        self.stack = []

    def start(self, transaction):
        if self.stack:
            parent = self.stack[-1]
            parent.add_child(transaction)
        else:
            if self.tree.get_msg_id() is None:
                self.tree.set_msg_id(self.factory.get_next_id())
            self.tree.set_msg(transaction)
        self.stack.append(transaction)

    def end(self, msg_manager, transaction):
        if self.stack:
            self.stack.pop()
            if not self.stack:
                tree = copy.copy(self.tree)
                self.tree.set_msg_id(None)
                self.tree.set_msg(None)
                msg_manager.flush(tree)
                return True
        return False
