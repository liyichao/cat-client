#!/usr/bin/env python
# coding: utf-8

from tracing.message_manager import MessageManager
from tracing.transaction import Transaction


class MessageProducer(object):
    def __init__(self):
        self.manager = MessageManager()

    def new_transaction(self, ttype, name):
        transaction = Transaction(ttype, name)
        self.manager.start(transaction)