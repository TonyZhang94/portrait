# -*- coding:utf-8 -*-

from DBparam import *


DBDefault = Outer99


class Entrance(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, pcid="4", cid="50012097", datamonth="201805"):
        self.__pcid = str(pcid)
        self.__cid = str(cid)
        self.__datamonth = str(datamonth)

    @property
    def pcid(self):
        return self.__pcid

    @property
    def cid(self):
        return self.__cid

    @property
    def datamonth(self):
        return self.__datamonth

    @property
    def params(self, option=3):
        if 3 == option:
            return self.__pcid, self.__cid, self.__datamonth
        else:
            return self.__pcid, self.__cid


class InstantiationError(Exception):
    def __init__(self):
        err = "Instantiation Is Not Allowed"
        Exception.__init__(self, err)


class Mode(object):
    stcLOCAL = True
    savePKL = True

    def __new__(cls, *args, **kwargs):
        raise InstantiationError


class Parameters(object):
    dim_targets = 100
    score_base = 50.0
    min_dim = 5
    floor_submarkets = 20

    def __new__(cls, *args, **kwargs):
        raise InstantiationError


class FileBase(object):
    info = "data/info_{name}_pcid{pcid}cid{cid}.csv"
    result = "result/pcid{pcid}cid{cid}/{name}.pkl"

    def __new__(cls, *args, **kwargs):
        raise InstantiationError


class EraseItem(object):
    erase_target = dict()
    erase_submarket = dict()

    wrong_all = []

    items = []
    items.extend(wrong_all)
    erase_target["50012097"] = set(items)

    items = []
    items.extend(wrong_all)
    erase_submarket["50012097"] = set(items)

    def __new__(cls, *args, **kwargs):
        raise InstantiationError


if __name__ == '__main__':
    try:
        m = Mode()
    except Exception as e:
        print(e)
