# -*- coding:utf-8 -*-

import _pickle
import inspect
import os

from portrait.settings import *
from portrait.tool.public import Entrance
import portrait.component.readData
from portrait.component.readData import RegisterDBException


def sum_freq(df):
    total = df["frequency"].sum()
    df["frequency"] = total
    return df[: 1]


def sum_score(df):
    total = df["frequency"].sum()
    tag, target = df["tag"].values[0], df["target"].values[0]
    df["score"], df["target"] = total, "%s-%s" % (tag, target)
    return df[: 1]


def dump(data, name):
    if Mode.savePKL:
        enter = Entrance()
        pcid, cid, _ = enter.params
        path = FileBase.result[: -10].format(pcid=pcid, cid=cid)
        try:
            os.makedirs(path)
        except (FileExistsError, FileNotFoundError) as e:
            print(path, "is exist")
        except Exception as e:
            raise e
        else:
            print("create", path, "success")
        finally:
            pass
        with open(FileBase.result.format(pcid=pcid, cid=cid, name=name), mode="wb") as fp:
            _pickle.dump(data, fp)


def load(name):
    enter = Entrance()
    pcid, cid, _ = enter.params
    with open(FileBase.result.format(pcid=pcid, cid=cid, name=name), mode="rb") as fp:
        data = _pickle.load(fp)
    return data


def read(src):
    funcs = {name: func for name, func in inspect.getmembers(
        portrait.component.readData, inspect.isfunction) if "_info" in name}
    try:
        return funcs["get_%s_info" % src]
    except KeyError:
        # print("Read Data Function Key Error:", "get_%s_info" % src)
        pass
    try:
        func = funcs["get_%ss_info" % src]
        # print("Read Data Function Key Is:", "get_%ss_info" % src)
        return func
    except KeyError:
        pass
    try:
        if "s" == src[-1]:
            func = funcs["get_%s_info" % src[: -1]]
            # print("Read Data Function Key Is:", "get_%s_info" % src[: -1])
            return func
    except KeyError:
        pass
    raise RegisterDBException


def make_trantab(src, dst=""):
    trantab = dict()
    for item in src:
        trantab[ord(item)] = dst
    return trantab


if __name__ == '__main__':
    Entrance(pcid="0", cid="0", datamonth="0")
    dump(1, "1")
