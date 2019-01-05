# -*- coding:utf-8 -*-

from portrait.tool.utils import *


class BuildPortraitMethod(object):
    def __init__(self):
        """"""

    def build(self, *args, **kwargs):
        """Action"""


class BuildModelFrame(BuildPortraitMethod):
    def build(self, info, hot_targets):
        info["model_target_ratings"] = info["model_target_ratings"].fillna("{}")
        model_portraits = dict()
        for k, v in info.iterrows():
            ratings = eval(v["model_target_ratings"])
            model_portraits[v["serial"]] = list()
            for tag, targets in ratings.items():
                for target, score in targets.items():
                    key = "%s-%s" % (tag, target)
                    if key in hot_targets.keys() and float(score) > Parameters.score_base:
                        model_portraits[v["serial"]].append([tag, target, float(score)])
        for k, v in info.iterrows():
            if Parameters.min_dim <= len(model_portraits[v["serial"]]):
                continue
            ratings, temp = eval(v["model_target_ratings"]), list()
            for tag, targets in ratings.items():
                for target, score in targets.items():
                    key = "%s-%s" % (tag, target)
                    if key in hot_targets.keys():
                        temp.append([tag, target, score])
            temp = sorted(temp, key=lambda x: x[2], reverse=True)
            short = Parameters.min_dim - len(model_portraits[v["serial"]])
            model_portraits[v["serial"]].extend(temp[: short])

        dump(model_portraits, "model_portraits")
        return model_portraits
