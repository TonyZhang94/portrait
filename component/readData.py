# -*- coding:utf-8 -*-

from portrait.tool.engine import Engine
from portrait.tool.decorator import *
from portrait.settings import *


class ReadDBException(Exception):
    """Choose Get Data From DB"""


class RegisterDBException(Exception):
    """Choose Get Data From DB"""


def read_data(src, fname, sql, db):
    try:
        if not src:
            raise ReadDBException
        df = pd.read_csv(fname, encoding="utf-8", index_col=0)
    except (FileExistsError, FileNotFoundError, ReadDBException) as flag:
        print(sql)
        engine = Engine()
        try:
            df = pd.read_sql_query(sql, engine(db))
        except Exception as e:
            raise e
        else:
            if flag.__doc__ != "Choose Get Data From DB":
                df.to_csv(fname, encoding="utf-8")
    except Exception as e:
        raise e
    return df


@logging
def get_targets_info(pcid, cid, datamonth=None, src=Mode.srcLOCAL):
    fname = FileBase.info.format(name="targets", pcid=pcid, cid=cid)
    fields = ["brand", "model", "tag", "target", "grade", "frequency"]
    field, table = ", ".join(fields), "comment.review_analysis_pcid{pcid}_cid{cid}".format(pcid=pcid, cid=cid)
    if datamonth is not None:
        sql = "SELECT {field} FROM {table} WHERE datamonth='{datamonth}';".format(
            field=field, table=table, datamonth=datamonth)
    else:
        sql = "SELECT {field} FROM {table};".format(field=field, table=table)
    return read_data(src, fname=fname, sql=sql, db="report_dg")


@logging
def get_ratings_info(pcid, cid, datamonth=None, src=Mode.srcLOCAL):
    fname = FileBase.info.format(name="ratings", pcid=pcid, cid=cid)
    fields = ["brand", "model", "model_target_ratings"]
    field, table = ", ".join(fields), "product_brain.product_brain_pcid{pcid}".format(pcid=pcid)
    if datamonth is not None:
        sql = "SELECT {field} FROM {table} WHERE datamonth='{datamonth}';".format(
            field=field, table=table, datamonth=datamonth)
    else:
        sql = "SELECT {field} FROM {table};".format(field=field, table=table)
    return read_data(src, fname=fname, sql=sql, db="report_dg")


@logging
def get_urls_info(pcid, cid, datamonth=None, src=Mode.srcLOCAL):
    fname = FileBase.info.format(name="model-urls", pcid=pcid, cid=cid)
    fields = ["brand", "model", "imageurl"]
    field, table = ", ".join(fields), "product_brain.product_brain_pcid{pcid}".format(pcid=pcid, cid=cid)
    if datamonth is not None:
        sql = "SELECT {field} FROM {table} WHERE cid='{cid}' and datamonth='{datamonth}';".format(
            field=field, table=table, cid=cid, datamonth=datamonth)
    else:
        sql = "SELECT {field} FROM {table} WHERE cid='{cid}';".format(field=field, table=table, cid=cid)
    return read_data(src, fname=fname, sql=sql, db="report_dg")


@logging
def get_submarkets_info(pcid, cid, datamonth=None, src=Mode.srcLOCAL):
    fname = FileBase.info.format(name="submarkets", pcid=pcid, cid=cid)
    fields = ["brand", "model", "biz30day", "total_sold_price", "submarket", "target_score", "sku"]
    field, table = ", ".join(fields), "product_brain.product_brain_pcid{pcid}".format(pcid=pcid, cid=cid)
    if datamonth is not None:
        sql = "SELECT {field} FROM {table} WHERE cid='{cid}' and datamonth='{datamonth}';".format(
            field=field, table=table, cid=cid, datamonth=datamonth)
    else:
        sql = "SELECT {field} FROM {table} WHERE cid='{cid}';".format(field=field, table=table, cid=cid)
    return read_data(src, fname=fname, sql=sql, db="report_dg")


@logging
def get_sku_info(pcid, cid, datamonth, src=Mode.srcLOCAL):
    fname = FileBase.info.format(name="sku", pcid=pcid, cid=cid)
    fields = ["brand", "model", "sku"]
    field, table = ", ".join(fields), "product_brain.product_brain_pcid{pcid}".format(pcid=pcid, cid=cid)
    if datamonth is not None:
        sql = "SELECT {field} FROM {table} WHERE cid='{cid}' and datamonth='{datamonth}';".format(
            field=field, table=table, cid=cid, datamonth=datamonth)
    else:
        sql = "SELECT {field} FROM {table} WHERE cid='{cid}';".format(field=field, table=table, cid=cid)
    return read_data(src, fname=fname, sql=sql, db="report_dg")


@logging
def get_sales_info(pcid, cid, datamonth=None, src=Mode.srcLOCAL):
    fname = FileBase.info.format(name="sale", pcid=pcid, cid=cid)
    fields = ["brand", "model", "price", "biz30day", "total_sold_price"]
    field, table = ", ".join(fields), "product_brain.product_brain_pcid{pcid}".format(pcid=pcid, cid=cid)
    if datamonth is not None:
        sql = "SELECT {field} FROM {table} WHERE cid='{cid}' and datamonth='{datamonth}';".format(
            field=field, table=table, cid=cid, datamonth=datamonth)
    else:
        sql = "SELECT {field} FROM {table} WHERE cid='{cid}';".format(field=field, table=table, cid=cid)
    return read_data(src, fname=fname, sql=sql, db="report_dg")
