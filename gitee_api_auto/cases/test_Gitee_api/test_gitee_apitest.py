#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: KyleYeung
# datetime:2022/8/8 17:27
# software: PyCharm

import allure
from tools.gitee_api import JkClient
import pytest
import time

GITEETOKEN = ''
GOODSID = ''
PRODUCTID = ''

@allure.feature('Gitee')
class TestControl(object):
    @pytest.mark.flaky(reruns=3, reruns_delay=10)
    @allure.story('获取登录token')
    @pytest.mark.parametrize("expected", [('"errmsg":"成功"')])
    def test_Gitee_login(self, log,url_Gitee_login,expected):
        """获取登录token"""
        global GITEETOKEN
        data ={
            "username": "gitee",
            "password": "qwer1234"
        }
        headers = url_Gitee_login["headers"]
        jk = JkClient()
        r = jk.requestData(url=url_Gitee_login["url"], json=data, headers=headers, reqtype='post')
        print(r[0].text)
        GITEETOKEN = r[0].json()['data']['token']
        assert r[0].status_code == 200
        assert expected in r[0].text

    @allure.story('商品搜索')
    @pytest.mark.parametrize("expected", [('"name":"3D纯棉护颈加翼记忆枕"')])
    def test_Gitee_GoodsSearch(self, log, url_Gitee_GoodsSearch,expected):
        """商品搜索"""
        global GOODSID
        data = {
            'keyword': "3D",
            'page': 1,
            'limit':10
        }
        headers = {'X-Litemall-Token':GITEETOKEN}
        jk = JkClient()
        r = jk.requestData(url=url_Gitee_GoodsSearch["url"], params=data, headers=headers, reqtype='get')
        print(r[0].text)
        GOODSID = r[0].json()['data']['list'][0]['id']
        assert r[0].status_code == 200
        assert expected in r[0].text

    @allure.story('获取商品详情')
    @pytest.mark.parametrize("expected", [('"goodsId":1064006')])
    def test_Gitee_GoodsDetails(self, log, url_Gitee_GoodsDetails, expected):
        """获取商品详情"""
        global PRODUCTID
        data = {
            'id': GOODSID
        }
        headers = {'X-Litemall-Token': GITEETOKEN}
        jk = JkClient()
        r = jk.requestData(url=url_Gitee_GoodsDetails["url"], params=data, headers=headers ,reqtype='get')
        print(r[0].text)
        PRODUCTID = r[0].json()['data']['productList'][0]['id']
        assert r[0].status_code==200
        assert expected in r[0].text


    @allure.story('添加商品到购物车')
    @pytest.mark.parametrize("expected", [('"errmsg":"成功"')])
    def test_Gitee_GoodsAdd(self, log, url_Gitee_GoodsAdd, expected):
        """添加商品到购物车"""
        data = {
            "goodsId": GOODSID,
            "number": 1,
            "productId": PRODUCTID
        }
        headers = {'X-Litemall-Token': GITEETOKEN}
        jk = JkClient()
        r = jk.requestData(url=url_Gitee_GoodsAdd["url"], json=data, headers=headers, reqtype='post')
        print(r[0].text)
        assert r[0].status_code == 200
        assert expected in r[0].text


    @allure.story('获取购物车列表')
    @pytest.mark.parametrize("expected", [('"goodsName":"3D纯棉护颈加翼记忆枕"')])
    def test_Gitee_GoodsCart(self, log, url_Gitee_GoodsCart,expected):
        """获取购物车列表接口"""
        time.sleep(3)
        data = {}
        headers = {'X-Litemall-Token':GITEETOKEN}
        jk = JkClient()
        r = jk.requestData(url=url_Gitee_GoodsCart["url"], json=data, headers=headers, reqtype='get')
        print(r[0].text)
        assert r[0].status_code == 200
        assert expected in r[0].text







