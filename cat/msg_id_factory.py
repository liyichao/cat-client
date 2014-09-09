#!/usr/bin/env python
# coding: utf-8


from util import time_in_hour


class MsgIdFactory(object):
    def __init__(self, domain=None, ip=None):
        self.domain = domain
        self.ip = ip
        self.timestamp = time_in_hour()
        self.index = 0

    def get_next_id(self):
        timestamp = time_in_hour()
        if timestamp != self.timestamp:
            self.index = 0
            self.timestamp = timestamp
        index = self.index
        self.index += 1

        return '{domain}-{ip}-{timestamp}-{index}'.format(domain=self.domain, ip=self.ip,
                                                          timestamp=self.timestamp, index=index)

