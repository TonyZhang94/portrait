# -*- coding:utf-8 -*-

from portrait.tool.decorator import *
from portrait.component.taksObj import *


def get_data(src):
    obj = ReadData()
    data = obj.process(src)
    return data


@logging
@ignore_warning
def select_targets(info, dim=Parameters.dim_targets):
    obj = SelectTargets()
    hot_targets = obj.process(info, dim=dim)
    dump(hot_targets, "hot_targets")
    return hot_targets


@logging
def build_model_portraits(info, hot_targets):
    obj = BuildPortrait()
    model_portraits = obj.process(info, hot_targets)
    dump(model_portraits, "model_portraits")
    return model_portraits


@logging
def store_portraits(model_portraits):
    obj = StorePortrait()
    obj.process(model_portraits)


if __name__ == '__main__':
    a = ReadData()
