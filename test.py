# -*- coding:utf-8 -*-

import _pickle

from portrait.settings import *
from portrait.tool.public import Entrance


if __name__ == '__main__':
    enter = Entrance(pcid="4", cid="50012097", datamonth="201805")
    pcid, cid, _ = enter.params
    name = "model_portraits"
    # name = "submarket_portraits"
    with open(FileBase.result.format(pcid=pcid, cid=cid, name=name), mode="rb") as fp:
        data = _pickle.load(fp)

    print(type(data))
    for k, v in data.items():
        print(k, v)
