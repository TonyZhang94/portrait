# -*- coding:utf-8 -*-


from portrait.tasks import *
from portrait.settings import *


class Manager(object):
    def __init__(self, pcid, cid, datamonth):
        Entrance(pcid=pcid, cid=cid, datamonth=datamonth)

    def run(self):
        target_info = get_data("targets")
        hot_targets = select_targets(target_info)

        ratings_info = get_data("ratings")
        model_portraits = build_model_portraits(ratings_info, hot_targets)

        # add sku, add brand, add url, add sales

        store_portraits(model_portraits)


if __name__ == '__main__':
    pcid = "4"
    cid = "50012097"
    datamonth = "201805"

    obj = Manager(pcid=pcid, cid=cid, datamonth=datamonth)
    obj.run()
