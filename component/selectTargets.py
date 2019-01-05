# -*- coding:utf-8 -*-


from portrait.tool.utils import *


class SelectMethod(object):
    def __init__(self):
        """"""

    def select(self, *args, **kwargs):
        """Action"""


class SelectByNomination(SelectMethod):
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


class SelectBySigned(SelectMethod):
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


if __name__ == '__main__':
    pass
