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
    return model_portraits


@logging
def append_features(model_portraits, info):
    obj = AppendFeatures()
    model_portraits = obj.process(model_portraits, info)
    return model_portraits


@logging
def store_portraits(model_portraits):
    obj = StorePortrait()
    obj.process(model_portraits)


@logging
def select_submarkets(submarkets_info):
    obj = SelectSubmarkets()
    sm_map, sm_hot, sm_all = obj.process(submarkets_info)
    dump(sm_map, "sm_map")
    dump(sm_hot, "sm_hot")
    dump(sm_all, "sm_all")
    return sm_hot.keys()


@logging
def reconstruct_info(targets_info, submarket_info, hot_targets, submarkets):
    obj = ReconstructInfo()
    info = obj.process(targets_info, submarket_info, hot_targets, submarkets)
    enter = Entrance()
    pcid, cid, _ = enter.params
    name = FileBase.info.format(name="reConsInfo", pcid=pcid, cid=cid)
    info.to_csv(name, encoding="utf-8")
    return info


@logging
def select_top_model(info, submarkets):
    obj = SelectTopModel()
    top_models_info = obj.process(info, submarkets)
    dump(top_models_info, "top_models_info")
    return top_models_info


@logging
def build_submarket_portraits(top_models_info, model_portraits):
    obj = BuildSubmarketPortraits()
    submarket_portraits = obj.process(top_models_info, model_portraits)
    dump(submarket_portraits, "submarket_portraits")
    return submarket_portraits


if __name__ == '__main__':
    a = ReadData()
