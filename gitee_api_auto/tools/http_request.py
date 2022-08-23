#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: KyleYeung
# datetime:2022/8/8 17:27
# software: PyCharm

import requests


# ----------------------------------------------------

def http_post(url, payload, headers, timeout=30):
    res = requests.request("POST", url, data=payload, headers=headers, timeout=timeout)
    return res


def http_get(url, payload, headers, querystring, timeout=30):
    res = requests.request("GET", url, data=payload, headers=headers, params=querystring, timeout=timeout)
    # 获取返回code
    code = res.status_code
    print('code', code)
    return res


def get_code(res):
    # 获取返回code
    code = res.status_code
    print('code：\n', code)


def get_json(res):
    # 获取返回json
    print('res.json：\n', res.json())
    return res.json()


def get_text(res):
    print('res.text：\n', res.text)
    return res.text


def get_time(res):
    # 获取响应执行时间,单位s
    time = res.elapsed.total_seconds()
    print('res.time：\n', res.elapsed.total_seconds())
    return time


def get_header(act):
    if act == "json":

        json_header = {
            'content-type': "application/json",
        }
        return json_header
    else:
        str_header = {
            'content-type': "application/x-www-form-urlencoded",
        }
        return str_header


def add_header(dict):
    headers = get_header("json")
    for k, v in dict.items():
        headers[k] = v
    return headers
