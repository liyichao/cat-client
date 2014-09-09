#!/usr/bin/env python
# coding: utf-8


class MsgTree(object):
    def __init__(self, domain=None, hostname=None, ip=None,
                 msg=None, msg_id=None, parent_msg_id=None, root_msg_id=None):
        self.domain = domain
        self.hostname = hostname
        self.ip = ip
        self.msg = msg
        self.msg_id = msg_id
        self.parent_msg_id = parent_msg_id
        self.root_msg_id = root_msg_id

    def get_domain(self):
        return self.domain

    def get_hostname(self):
        return self.hostname

    def get_ip(self):
        return self.ip

    def set_msg(self, msg):
        self.msg = msg

    def get_msg(self):
        return self.msg

    def get_msg_id(self):
        return self.msg_id

    def set_msg_id(self, msg_id):
        self.msg_id = msg_id

    def get_parent_msg_id(self):
        return self.parent_msg_id

    def get_root_msg_id(self):
        return self.root_msg_id
