#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: KyleYeung
# datetime:2022/8/8 17:27
# software: PyCharm


import pytest
import time
import os
from config.prod.config import RunConfig

# 项目路径
pro_path = os.path.dirname(os.path.abspath(__file__))

# 测试用例目录
test_case = os.getenv("testcase", None)
if test_case is None:
    test_case = 'cases'

# 执行环境
env = os.getenv("environment", None)
if env is None:
    env = 'test'

# 报告生成地址：
result_path = './allure-results'
html_path = './html-report'

def main(test_c=None):
    # 优先传进来的用例路径
    tc = test_c or test_case
    # 修改执行次数的话，修改这边的500
    pytest.main(
        ["--env={}".format(env),
         "{}".format(tc),
         # "--reruns=1", "--reruns-delay=5",
         # "--count=1", "--repeat-scope=session",
         "--alluredir", result_path,
         "-vs"
         ]
    )


def run():

    print("回归模式，开始执行！")
    starttime = time.strftime("%Y-%m-%d %H_%M_%S")
    print("开始时间：%s" % starttime)
    # 删除历史报告
    # if os.path.exists(html_path + "/" + RunConfig.reportname): os.remove(html_path + "/" + RunConfig.reportname)
    # 执行pytest开始测试
    main(test_case)
    endtime = time.strftime("%Y-%m-%d %H_%M_%S")
    print("结束时间：%s" % endtime)
    print("运行结束，生成测试报告！")
    print (pro_path + u'\\' + html_path[:-2] + u'\\' + RunConfig.reportname)
    print (html_path + "/" + RunConfig.reportname)

if __name__ == "__main__":
    run()
