# -*- coding:utf-8 -*-
import itertools

import pandas as pd
import re

from portrait.tool.utils import *


class PreProcessMethod(object):
    def __init__(self):
        self.blanks = [" ", "\\xa0"]
        # self.move = dict.fromkeys([ord(c) for c in u"\xa0\n\t"])

    def pre_process(self, **kwargs):
        """Pre Process Data"""

    def no_blank(self, text):
        for blank in self.blanks:
            text = text.replace(blank, "")
        if "\\xa0" in text:
            print(text)
        # text = text.translate(self.move)
        # while "\xa0" == text[0]:
        #     print(111)
        #     print(text)
        #     text = text[1:]
        #     print(text)
        # while "\xa0" == text[-1]:
        #     text = text[: -1]
        return text.strip()


class CombineBrandModel(PreProcessMethod):
    def pre_process(self, df):
        # super().pre_process(df)
        df["serial"] = ""
        for k, v in df.iterrows():
            brand = self.no_blank(v["brand"])
            model = self.no_blank(v["model"])
            df.at[k, ["serial"]] = "%s-%s" % (brand, model)
        return df


class ClearNone(PreProcessMethod):
    def pre_process(self, df):
        """Fill None"""
        return df


class ReConstructTargetSubmarketInfo(PreProcessMethod):
    def pre_process(self, info_target, info_submarket, target_hot, sm_hot):
        neg_list = info_target["grade"] == -1
        info_target.loc[neg_list, ["frequency"]] = -info_target.loc[neg_list, ["frequency"]]
        zero_list = info_target["grade"] == 0
        info_target.loc[zero_list, ["frequency"]] = 0
        df_score = info_target[["brand", "model", "tag", "target", "frequency", "serial"]] \
            .groupby(["brand", "model", "tag", "target"]).apply(sum_score).reset_index(drop=True)

        dict_score = dict()
        for k, v in df_score.iterrows():
            model = v["serial"]
            target = v["target"]
            try:
                type(dict_score[model])
            except KeyError:
                dict_score[model] = dict()
            finally:
                dict_score[model][target] = v["score"]

        columns = ["serial", "brand", "model", "biz", "ts_price", "submarket", "title"]
        df_res = pd.DataFrame([], columns=columns)
        for k, v in info_submarket.iterrows():
            brand, model, serial = [v["brand"]], [v["model"]], [v["serial"]]
            biz, ts_price = [v["biz30day"]], [v["total_sold_price"]]
            try:
                title = [re.search(r"(?<='书名': ').*?(?=', ')", str(v["sku"])).group()]
            except AttributeError:
                title = [""]
            trantab = make_trantab("{} '")
            sm_list = [item.split(":")[1] for item in str(v["submarket"]).translate(trantab).split(",")]
            submarkets = [x for x in sm_list if x in sm_hot]

            values = list(itertools.product(serial, brand, model, biz, ts_price, submarkets, title))
            df_sku = pd.DataFrame(values, columns=columns)

            # df_target_score = df_score[(df_score["brand"] == v["brand"]) & (df_score["model"] == v["model"])]
            values = list()
            try:
                model = v["serial"]
                for key, value in dict_score[model].items():
                    if key in target_hot.keys():
                        values.append([key, int(dict_score[model][key])])
            except KeyError:
                values.append(["", 0])
            df_target = pd.DataFrame(values, columns=["target", "score"])
            df_target["brand"], df_target["model"] = v["brand"], v["model"]
            df_merge = pd.merge(df_sku, df_target,
                                how="left", on=["brand", "model"])
            df_res = df_res.append(df_merge, ignore_index=True)

        df_res["target"] = df_res["target"].fillna("")
        df_res["score"] = df_res["score"].fillna(0)
        del df_res["title"]
        return df_res


if __name__ == '__main__':
    pass
