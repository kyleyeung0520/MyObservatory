#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: KyleYeung
# datetime:2022/8/8 17:27
# software: PyCharm


import re
import sys
import time
import urllib.parse
import requests


# 当前使用的python版本
pythonversion=sys.version[0]
# 判断是python3则重写unicode方法

if sys.version[0]=='3':
    def unicode(s):
        # python3则转为字符串
        return str(s)


class JkClient(object):

    def __init__(self, logcode='utf-8'):
        self.logcode=logcode

    def requestData(self, url,data=None,headers=None,cookies=None,
                    params=None, files=None,
                    auth=None, timeout=60, allow_redirects=True, proxies=None,
                    hooks=None, stream=None, verify=None, cert=None, json=None,
                    reqtype='post', pathname=None, downloadbz=False,debug=True, **kwargs):
        '''
        通用请求，获取数据、cookies等
        :param url: 登录请求接口
        :param headers: 请求头信息
        :param data: 请求参数
        :param reqtype: 请求方法：port、get
        :param pathname: 下载文件名（包括路径）
        :param downloadbz: 下载的标志，True下载，False不下载
        :return: (请求响应对象, 请求session响应对象, 请求响应Cookie值)
        '''
        # multipart/form-data数据类型特殊处理
        try:
            if 'multipart/form-data' in headers['Content-Type']:
                try:
                    print (u'检测到headers数据类型为：multipart/form-data')
                    from requests_toolbelt import MultipartEncoder
                    data = MultipartEncoder(fields=data)
                    headers['Content-Type'] = data.content_type
                except:
                    print (u'处理multipart/form-data数据异常！')
        except:
            pass
        try:
            # 打印分割线
            if debug: print(u'# ########################################################\n# 请求相关数据开始打印')
            # 打印参数
            if debug:
                print (u'# 请求的url和参数和headers如下：')
                print(url)
                if data:
                    print (u'参数：', data)
                elif params:
                    print (u'参数：', params)
                elif json:
                    print (u'参数：', json)
                elif files:
                    print (u'参数：', files)
            # 如果是get请求，且带参数请求。进行url编码后转为链接。
            if reqtype=='get' and '?' not in url and data:
                if type(data) == type({}):
                    url = url + '?'
                    for key in data:
                        url = u'%s%s=%s&' % (url, urllib.parse.quote(unicode(key).encode('utf8')), urllib.parse.quote(unicode(data[key]).encode('utf8')))
                    url = url[:-1]
                if debug: print (url)
            # cookies处理，如果是字符串类型。
            if type(cookies) == type(''):
                if headers is None: headers = {}
                headers['Cookie'] = cookies
                cookies = None
            # 打印参数
            if debug: print(u'headers：', headers)
            # 打印分割线
            if debug: print(u'# 请求相关数据打印完毕\n# ########################################################')
            # 请求类型处理
            req = requests.Session()
            reqtype = 'req.' + reqtype.lower()
            t0 = time.time()
            # 发送请求
            r = eval(reqtype)(
                url=url,
                data=data,
                headers=headers,
                cookies=cookies,
                params=params,
                files=files,
                auth=auth,
                timeout=timeout,
                allow_redirects=allow_redirects,
                proxies=proxies,
                hooks=hooks,
                stream=stream,
                verify=verify,
                cert=cert,
                json=json
                )
            t1 = time.time()
            t = t1 - t0
            # 判断是否下载文件
            if downloadbz:
                with open(pathname, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                            f.flush()
                f.close()
            # 获取cookies
            cookies_nr = req.cookies
            cookies_list = re.split(r'\s', str(cookies_nr))
            nr = ''
            for c in cookies_list:
                if '=' in c:
                    nr = nr + c + u'; '

            # 关闭链接
            req.close()
            # 返回（响应对象、session对象、cookiesstr、响应时长）
            return (r,req,nr,t)
        except:
            print(u"请求处理出错：")
