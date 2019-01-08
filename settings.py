# -*- coding:utf-8 -*-

from DBparam import *

# class Outer99(object):
#     host = $ip$
#     port = $port$
#     user = $username$
#     password = $password$
#
#     DB = dict()
#     DB["standard_library"] = "standard_library"
#     DB["fact_library"] = "fact_library"
#     DB["zhuican_web"] = "zhuican_web"
#     DB["raw_mj_category"] = "raw_mj_category"
#     DB["report_dg"] = "report_dg"
#     DB["raw_tb_comment_notag"] = "raw_tb_comment_notag"


DBDefault = Outer99


class InstantiationError(Exception):
    def __init__(self):
        err = "Instantiation Is Not Allowed"
        Exception.__init__(self, err)


class Mode(object):
    """For Test"""
    stcLOCAL = True
    savePKL = True
    storePortrait = False
    # storePortrait = True

    """For Use"""
    # stcLOCAL = False
    # savePKL = False
    # storePortrait = True

    def __new__(cls, *args, **kwargs):
        raise InstantiationError


class Parameters(object):
    dim_targets = 100
    score_base = 50.0
    min_dim = 5
    submarkets_threshold = 20
    top_num_submarkets_as_standard = 20
    top_per_submarkets_as_standard = 0.2
    submarkets_sort_key = "biz"

    def __new__(cls, *args, **kwargs):
        raise InstantiationError


class FileBase(object):
    info = "data/info_{name}_pcid{pcid}cid{cid}.csv"
    result = "result/pcid{pcid}cid{cid}/{name}.pkl"

    def __new__(cls, *args, **kwargs):
        raise InstantiationError


class EraseItem(object):
    erase_target = dict()
    erase_submarket = dict()

    wrong_all = []

    items = []
    items.extend(wrong_all)
    erase_target["50012097"] = set(items)

    items = []
    items.extend(wrong_all)
    erase_submarket["50012097"] = set(items)

    def __new__(cls, *args, **kwargs):
        raise InstantiationError


class FeatureType(object):
    sale_type = ("price", "aver_price", "biz30day", "total_sold_price")
    sale_type = set(sale_type)

    continuous_type = []
    continuous_type = set(continuous_type)

    mul_con_type = []
    mul_con_type = set(mul_con_type)

    # default type
    discrete_type = []
    discrete_type = set(discrete_type)

    mul_dis_type = ["功能", "使用功能", "产品功能", "颜色", "颜色分类"]
    mul_dis_type = set(mul_dis_type)

    def __new__(cls, *args, **kwargs):
        raise InstantiationError


if __name__ == '__main__':
    try:
        m = Mode()
    except Exception as e:
        print(e)
