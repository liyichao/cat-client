#!/usr/bin/env python
# coding: utf-8

import time


class Message(object):
    def __init__(self, mtype, name):
        self.type = mtype
        self.name = name
        self.status = "0"
        self.timestamp = time.time()

    def get_timestamp(self):
        return self.timestamp

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_status(self):
        pass
