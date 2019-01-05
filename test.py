# -*- coding:utf-8 -*-

import _pickle

from portrait.settings import *


if __name__ == '__main__':
    enter = Entrance()
    pcid, cid, _ = enter.params
    name = "model_portraits"
    with open(FileBase.result.format(pcid=pcid, cid=cid, name=name), mode="rb") as fp:
        data = _pickle.load(fp)

    print(type(data))
    for k, v in data.items():
        print(k, v)
