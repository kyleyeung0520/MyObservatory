#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: KyleYeung
# datetime:2022/8/8 17:27
# software: PyCharm

import pytest
from tools.Logger import Log
import time
import sys
from py.xml import html
from config.prod.config import RunConfig

client = None


@pytest.fixture(scope='session')
def log():
    log = Log(logger=__name__)
    return log


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")

# ################################
# pytest中pytest-html生成html报告

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """html报告表头，增加2列，1列测试时间，2列用例名称即用例的注释"""
    try:
        cells.insert(2, html.th('测试时间', class_='sortable time', col='time'))
        cells.insert(2, html.th('用例名称', class_='sortable description', col='description'))
        cells.pop()
    except:
        sys.exc_info()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    """html报告内容，增加2列，1列测试时间，2列用例名称即用例的注释"""
    try:
        cells.insert(2, html.td(report.starttime, class_='col-time'))
        cells.insert(2, html.td(report.description, class_='col-description'))
        cells.pop()
    except:
        sys.exc_info()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """html报告增加2列，1列测试时间，2列用例名称即用例的注释"""
    try:
        starttime = time.strftime("%Y-%m-%d %H:%M:%S")
        outcome = yield
        report = outcome.get_result()
        report.description = str(item.function.__doc__)
        report.starttime = starttime
    except:
        sys.exc_info()

def pytest_collection_modifyitems(items):
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        # item._nodeid = JkClient.decodeUnicode(item._nodeid)
# ################################

@pytest.fixture()
def url_Gitee_login():
    req= {}
    req["url"] = RunConfig.url_Gitee_Login
    req["headers"] = {'Content-Type':"application/json; charset=utf-8"}
    return req

@pytest.fixture()
def url_Gitee_GoodsSearch():
    req= {}
    req["url"] = RunConfig.url_Gitee_GoodsSearch
    return req

@pytest.fixture()
def url_Gitee_GoodsDetails():
    req= {}
    req["url"] = RunConfig.url_Gitee_GoodsDetails
    return req

@pytest.fixture()
def url_Gitee_GoodsAdd():
    req= {}
    req["url"] = RunConfig.url_Gitee_GoodsAdd
    return req

@pytest.fixture()
def url_Gitee_GoodsCart():
    req= {}
    req["url"] = RunConfig.url_Gitee_GoodsCart
    return req











