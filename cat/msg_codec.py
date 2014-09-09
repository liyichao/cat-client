#!/usr/bin/env python
# coding: utf-8

import struct
from cat.transaction import Transaction
import datetime


class PlainTextMsgCodec(object):
    VERSION = "PT1"
    DEFAULT = 0
    WITHOUT_STATUS = 1
    WITH_DURATION = 2


    @classmethod
    def encode(cls, msg_tree):
        buf = [cls.encode_header(msg_tree)]
        if msg_tree.get_msg() is not None:
            buf.append(cls.encode_msg(msg_tree.get_msg()))
        buf = ''.join(buf)
        size = struct.pack('!i', len(buf))
        return size + buf

    @classmethod
    def encode_header(cls, msg_tree):
        header = "{version}\t{domain}\t{hostname}\t{ip}\t" \
                 "{thread_group_name}\t{thread_id}\t{thread_name}\t" \
                 "{msg_id}\t{parent_msg_id}\t{root_msg_id}\t{session_token}\n".\
            format(version=cls.VERSION,
                   domain=msg_tree.get_domain(),
                   hostname=msg_tree.get_hostname(),
                   ip=msg_tree.get_ip(),
                   thread_group_name="thread_group",
                   thread_id="thread_id",
                   thread_name="thread_name",
                   msg_id=msg_tree.get_msg_id(),
                   parent_msg_id=msg_tree.get_parent_msg_id(),
                   root_msg_id=msg_tree.get_root_msg_id(),
                   session_token="session_token")
        return header

    @classmethod
    def encode_msg(cls, msg):
        if isinstance(msg, Transaction):
            children = msg.get_children()
            if not children:
                return cls.encode_line(msg, 'A', cls.WITH_DURATION)
            else:
                buf = [cls.encode_line(msg, 't', cls.WITHOUT_STATUS)]
                for child in children:
                    buf.append(cls.encode_msg(child))
                buf.append(cls.encode_line(msg, 'T', cls.WITH_DURATION))
                return ''.join(buf)

    @classmethod
    def encode_line(cls, msg, msg_type, policy):
        buf = [msg_type]
        if msg_type == 'T':
            buf.append(cls.format_date(msg.get_timestamp() + msg.get_duration()))
        else:
            buf.append(cls.format_date(msg.get_timestamp()))
        buf.append('\t{type}\t{name}\t'.format(type=msg.get_type(), name=msg.get_name()))
        #TODO



    @classmethod
    def format_date(cls, timestamp):
        return datetime.datetime.fromtimestamp(round(timestamp, 3)).strftime("%Y-%m-%d %H:%M:%S.%f")





