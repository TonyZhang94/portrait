# -*- coding:utf-8 -*-


class Quantity(object):
    __counter = 0

    def __init__(self, interface):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = "_{}#{}".format(prefix, index)
        self.interface = interface
        cls.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value is None:
            return
        if isinstance(value, self.interface):
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError("Parameter Must Be", self.interface.__name__)
