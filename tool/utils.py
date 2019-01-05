# -*- coding:utf-8 -*-

import _pickle

from portrait.settings import *


def sum_freq(df):
    total = df["frequency"].sum()
    df["frequency"] = total
    return df[:1]


def dump(data, name):
    if Mode.savePKL:
        enter = Entrance()
        pcid, cid, _ = enter.params
        with open(FileBase.result.format(pcid=pcid, cid=cid, name=name), mode="wb") as fp:
            _pickle.dump(data, fp)


def load(name):
    enter = Entrance()
    pcid, cid, _ = enter.params
    with open(FileBase.result.format(pcid=pcid, cid=cid, name=name), mode="rb") as fp:
        data = _pickle.load(fp)
    return data
