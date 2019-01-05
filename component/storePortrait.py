# -*- coding:utf-8 -*-

from portrait.tool.utils import *


class StoreMethod(object):
    def __init__(self):
        """"""

    def store(self, *args, **kwargs):
        """Action"""


class StoreTreeFrame(StoreMethod):
    def store(self, model_portraits):
        enter = Entrance()
        pcid, cid, _ = enter.params
        for name, attrs in model_portraits.items():
            base = '{"name": "' + name + '", "children":['
            file = FileBase.result.format(
                pcid=pcid, cid=cid, name="tree-"+name.replace("/", " ")).replace(".pkl", ".json")
            with open(file, mode="w+", encoding="utf-8") as fp:
                val = ""
                for attr in attrs:
                    if 2 == len(attr):
                        val = val + "{" + '"name": "{key}: {val}"'.format(
                            key=attr[0], val=attr[1]) + "},"
                    elif 3 == len(attr):
                        val = val + "{" + '"name": "{key1} {key2}: {val}"'.format(
                            key1=attr[0], key2=attr[1], val=attr[2]) + "},"
                    else:
                        raise Exception("portrait attr error")
                context = base + val[: -1] + "]}"
                fp.write(context)


class StoreToDB(StoreMethod):
    def store(self, model_portraits):
        pass


if __name__ == '__main__':
    pass
