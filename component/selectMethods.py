# -*- coding:utf-8 -*-


from portrait.tool.utils import *


class SelectMethod(object):
    def __init__(self):
        """"""

    def select(self, *args, **kwargs):
        """Action"""


class SelectTargetsByNomination(SelectMethod):
    def select(self, info, dim=Parameters.dim_targets):
        info = info[["tag", "target", "grade", "frequency"]]
        abs_freq = info.groupby(["tag", "target"]).apply(sum_freq) \
            .sort_values(["frequency"], ascending=False).drop(columns=["grade"]).reset_index(drop=True)

        targets, hot_targets, serial = dict(), dict(), 0
        for k, v in abs_freq.iterrows():
            key = "%s-%s" % (v["tag"], v["target"])
            if key in EraseItem.erase_target:
                continue
            targets[key] = serial
            if k < dim:
                hot_targets["%s-%s" % (v["tag"], v["target"])] = serial
            else:
                break
            serial += 1
        return hot_targets


class SelectTargetsBySigned(SelectMethod):
    def select(self, info, dim=Parameters.dim_targets):
        info = info[["tag", "target", "grade", "frequency"]]
        neg_list = info["grade"] == -1
        info.loc[neg_list, ["frequency"]] = -info.loc[neg_list, ["frequency"]]
        zero_list = info["grade"] == 0
        info.loc[zero_list, ["frequency"]] = 0
        sign_freq = info.groupby(["tag", "target"]).apply(sum_freq) \
            .sort_values(["frequency"], ascending=False).drop(columns=["grade"]).reset_index(drop=True)

        targets, hot_targets, serial = dict(), dict(), 0
        for k, v in sign_freq.iterrows():
            key = "%s-%s" % (v["tag"], v["target"])
            if key in EraseItem.erase_target:
                continue
            targets[key] = serial
            if k < dim:
                hot_targets["%s-%s" % (v["tag"], v["target"])] = serial
            else:
                break
            serial += 1
        return hot_targets


class SelectSubmarketsByNomination(SelectMethod):
    def select(self, info, dim):
        sm_jsons = info["submarket"].values
        sm_map, sm_hot = dict(), dict()
        trantab = make_trantab("{} '")
        for line in sm_jsons:
            items = str(line).translate(trantab).split(",")
            for item in items:
                sm_id, sm_name = item.split(":")
                if sm_name in EraseItem.erase_submarket:
                    continue
                sm_map[sm_name] = sm_id
                sm_hot.setdefault(sm_name, 1)
                sm_hot[sm_name] += 1
        sm_hot = sorted(sm_hot.items(), key=lambda x: x[1], reverse=True)

        sm_all = {sm_name: num for sm_name, num in sm_hot}
        sm_hot = {sm_name: num for sm_name, num in sm_hot if num > dim}
        return sm_map, sm_hot, sm_all


class SelectTopModelMethod(SelectMethod):
    def select(self, info, submarkets):
        info = info.drop_duplicates(["brand", "model", "submarket"])
        models = dict()
        for submarket in submarkets:
            info_bak = info[info["submarket"] == submarket].sort_values([Parameters.submarkets_sort_key],
                                                                        ascending=False)[
                       : Parameters.top_num_submarkets_as_standard]
            for k, v in info_bak.iterrows():
                models.setdefault(submarket, []).append(v["serial"])
        return models


if __name__ == '__main__':
    pass
