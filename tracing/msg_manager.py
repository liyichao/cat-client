#!/usr/bin/env python
# coding: utf-8

from message_id_factory import MessageIdFactory


class MessageManager(object):
    def __init__(self):
        self.factory = MessageIdFactory

    def end(self, transaction):
        pass

    def start(self, transaction):
        pass


class Context(object):
    def __init__(self):
        self.m_tree