# -*- coding:utf-8 -*-

from portrait.component.readData import *
from portrait.tool.public import Quantity
from portrait.component.clearData import *
from portrait.component.selectTargets import *
from portrait.component.buildPortrait import *
from portrait.component.storePortrait import *
from portrait.tool.utils import *


class ReadData(object):
    clearObj = Quantity(ClearMethod)

    def __init__(self):
        self.clearObj = None

    def process(self, src):
        enter = Entrance()
        df = read(src)(*enter.params)
        self.clearObj = CombineBrandModel()
        df = self.clearObj.clear(df)
        return df


class SelectTargets(object):
    selectObj = Quantity(SelectMethod)

    def __init__(self):
        self.selectObj = None

    def process(self, info, dim):
        self.selectObj = SelectByNomination()
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


class StorePortrait(object):
    storeObj = Quantity(StoreMethod)

    def __init__(self):
        self.storeObj = None

    def process(self, model_portraits):
        self.storeObj = StoreTreeFrame()
        self.storeObj.store(model_portraits)
