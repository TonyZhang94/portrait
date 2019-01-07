# -*- coding:utf-8 -*-

from portrait.tool.utils import *


class AppendMethod(object):
    def __init__(self):
        """"""

    def append(self, *args, **kwargs):
        """Action"""


class AppendMethodOne(AppendMethod):
    def append(self, model_portraits, info):
        columns = [col for col in info.columns if col not in ("brand", "model", "serial")]
        json_cols = set(["sku"])
        for k, v in info.iterrows():
            for col in columns:
                if col not in json_cols:
                    model_portraits[v["serial"]].append([col, v[col]])
                else:
                    line = v[col]
                    if not line:
                        continue
                    items = eval(line.replace("\\xa0", " "))
                    for key, val in items.items():
                        if key in FeatureType.mul_dis_type or key in FeatureType.mul_con_type:
                            val = val.replace("、", " ").replace("，", " ").replace(",", " ")
                            sub_vals = val.split()
                            for sub_val in sub_vals:
                                model_portraits[v["serial"]].append([key, sub_val])
                        else:
                            model_portraits[v["serial"]].append([key, val])
