#!/usr/bin/env python
# coding: utf-8

from tracing.message_producer import MessageProducer


class Trace(object):
    _instance = None

    def __init__(self):
        self.producer = MessageProducer()
        pass

    @staticmethod
    def initialize():
        Trace._instance = Trace()

    @classmethod
    def get_producer(cls):
        return cls._instance.producer

    @classmethod
    def new_transaction(cls, ttype, name):
        cls.get_producer().new_transaction(ttype, name)

    @classmethod
    def log_event(cls, etype, name, status, key_values):
        """Logs interesting event.
        :param etype: event type, examples: URL.Server
        :param name: event name, examples: serverIp
        :param status: Event.SUCCESS or Event.FAILED
        :param key_values: key1=value1&key2=value2
        """
        cls.get_producer().log_event(etype, name, status, key_values)
