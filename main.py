# -*- coding:utf-8 -*-


from portrait.tasks import *
from portrait.tool.public import *


class Manager(object):
    def __init__(self, pcid, cid, datamonth):
        Entrance(pcid=pcid, cid=cid, datamonth=datamonth)

    def run(self):
        targets_info = get_data("targets")
        hot_targets = select_targets(targets_info)

        ratings_info = get_data("ratings")
        model_portraits = build_model_portraits(ratings_info, hot_targets)

        sales_info = get_data("sales")
        append_features(model_portraits, sales_info)

        sku_info = get_data("sku")
        append_features(model_portraits, sku_info)

        urls_info = get_data("urls")
        append_features(model_portraits, urls_info)
        dump(model_portraits, "model_portraits")

        store_portraits(model_portraits)

        submarkets_info = get_data("submarkets")
        submarkets = select_submarkets(submarkets_info)

        info = reconstruct_info(targets_info, submarkets_info, hot_targets, submarkets)

        top_models_info = select_top_model(info, submarkets)
        submarket_portraits = build_submarket_portraits(top_models_info, model_portraits)

        store_portraits(submarket_portraits)


if __name__ == '__main__':
    pcid = "4"
    cid = "50012097"
    datamonth = "201805"

    obj = Manager(pcid=pcid, cid=cid, datamonth=datamonth)
    obj.run()
