# -*- coding:utf-8 -*-
import collections

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
            model_portraits[v["serial"]] = [["brand", v["brand"]], ["model", v["model"]]]
            for tag, targets in ratings.items():
                for target, score in targets.items():
                    key = "%s-%s" % (tag, target)
                    if key in hot_targets.keys() and float(score) > Parameters.score_base:
                        model_portraits[v["serial"]].append(["%s %s" % (tag, target), float(score)])
        for k, v in info.iterrows():
            if Parameters.min_dim <= len(model_portraits[v["serial"]]):
                continue
            ratings, temp = eval(v["model_target_ratings"]), list()
            for tag, targets in ratings.items():
                for target, score in targets.items():
                    key = "%s-%s" % (tag, target)
                    if key in hot_targets.keys():
                        temp.append(["%s %s" % (tag, target), score])
            temp = sorted(temp, key=lambda x: x[1], reverse=True)
            short = Parameters.min_dim - len(model_portraits[v["serial"]])
            model_portraits[v["serial"]].extend(temp[: short])

        dump(model_portraits, "model_portraits")
        return model_portraits


class BuildSubMarketFrame(BuildPortraitMethod):
    def build(self, top_models_info, model_portraits):
        submarket_portrait = dict()
        for submarket, models in top_models_info.items():
            data, attrs = dict(), set()
            submarket_portrait[submarket] = list()
            for model in models:
                data[model] = dict()
                for item in model_portraits[model]:
                    key, val = item
                    if key in FeatureType.mul_dis_type or key in FeatureType.mul_con_type:
                        data[model].setdefault(key, []).append(val)
                    else:
                        data[model][key] = val
                attrs |= set(data[model].keys())
            useless = ["brand", "model", "imageurl"]
            attrs -= set(useless)
            for attr in attrs:
                vals = list()
                for model in models:
                    try:
                        vals.append(data[model][attr])
                    except KeyError:
                        pass
                try:
                    avg = round(sum(vals) / len(vals), 2)
                    submarket_portrait[submarket].append([attr, avg])
                except TypeError:
                    if attr in FeatureType.mul_dis_type or attr in FeatureType.mul_con_type:
                        sub_vals = list()
                        for val in vals:
                            sub_vals.extend(val)
                        vals = sub_vals
                    ct = collections.Counter(vals)
                    items = ct.most_common(5)
                    for item in items:
                        if "颜色" in attr:
                            if 5 < len(item[0]):
                                continue
                        submarket_portrait[submarket].append([attr, item[0]])
        return submarket_portrait


