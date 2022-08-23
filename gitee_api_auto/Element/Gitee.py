#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tools.gitee_api import JkClient

class GiteeGetToken(object):

    def get_token(self, url=None, data=None, headers=None):
        url = url or 'https://litemall.hogwarts.ceshiren.com/wx/auth/login'
        data = data or{"username": "gitee","password": "qwer1234"}
        headers = headers or{"Content-Type": "application/json; charset=utf-8"}
        jk = JkClient()
        r = jk.requestData(url=url, json=data, headers=headers)
        token = r[0].json()['data']['token']
        return token


if __name__ == "__main__":
    a = GiteeGetToken()
    b = a.get_token()
    token = b[0].json()['data']['token']
    print(token)




