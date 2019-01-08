# -*- coding:utf-8 -*-

from portrait.settings import Mode
from portrait.component.readData import *
from portrait.tool.public import Quantity, Entrance
from portrait.component.preProcessData import *
from portrait.component.selectMethods import *
from portrait.component.buildPortrait import *
from portrait.component.appendFeatures import *
from portrait.component.storePortrait import *
from portrait.tool.utils import *


class ReadData(object):
    clearObj = Quantity(PreProcessMethod)

    def __init__(self):
        self.clearObj = None

    def process(self, src):
        enter = Entrance()
        df = read(src)(*enter.params)
        self.clearObj = CombineBrandModel()
        df = self.clearObj.pre_process(df)
        return df


class SelectTargets(object):
    selectObj = Quantity(SelectMethod)

    def __init__(self):
        self.selectObj = None

    def process(self, info, dim):
        self.selectObj = SelectTargetsByNomination()
        hot_targets = self.selectObj.select(info, dim=dim)
        return hot_targets


class BuildPortrait(object):
    buildObj = Quantity(BuildPortraitMethod)

    def __init__(self):
        self.buildObj = None

    def process(self, info, hot_targets):
        self.buildObj = BuildModelFrame()
        model_portraits = self.buildObj.build(info, hot_targets)
        return model_portraits


class AppendFeatures(object):
    appendObj = Quantity(AppendMethod)

    def __init__(self):
        self.appendObj = None

    def process(self, model_portraits, info):
        self.appendObj = AppendMethodOne()
        model_portraits = self.appendObj.append(model_portraits, info)
        return model_portraits


class StorePortrait(object):
    storeObj = Quantity(StoreMethod)

    def __init__(self):
        self.storeObj = None

    def process(self, model_portraits):
        if Mode.storePortrait:
            self.storeObj = StoreTreeFrame()
        else:
            self.storeObj = StoreToNothing()
        self.storeObj.store(model_portraits)


class SelectSubmarkets(object):
    selectObj = Quantity(SelectMethod)

    def __init__(self):
        self.selectObj = None

    def process(self, info, dim=Parameters.submarkets_threshold):
        self.selectObj = SelectSubmarketsByNomination()
        sm_map, sm_hot, sm_all = self.selectObj.select(info, dim)
        return sm_map, sm_hot, sm_all


class ReconstructInfo(object):
    infoObj = Quantity(PreProcessMethod)

    def __init__(self):
        self.infoObj = None

    def process(self, targets_info, submarket_info, hot_targets, submarkets):
        self.infoObj = ReConstructTargetSubmarketInfo()
        info = self.infoObj.pre_process(targets_info, submarket_info, hot_targets, submarkets)
        return info


class SelectTopModel(object):
    selectObj = Quantity(SelectMethod)

    def __init__(self):
        self.selectObj = None

    def process(self, info, submarkets):
        self.selectObj = SelectTopModelMethod()
        top_models_info = self.selectObj.select(info, submarkets)
        return top_models_info


class BuildSubmarketPortraits(object):
    buildObj = Quantity(BuildPortraitMethod)

    def __init__(self):
        self.buildObj = None

    def process(self, top_models_info, model_portraits):
        self.buildObj = BuildSubMarketFrame()
        submarket_portraits = self.buildObj.build(top_models_info, model_portraits)
        return submarket_portraits
