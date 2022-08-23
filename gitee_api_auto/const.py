#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: KyleYeung
# datetime:2022/8/8 17:27
# software: PyCharm

import sys
import os


class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value


sys.modules[__name__] = _const()

path = os.path.dirname(os.path.realpath(__file__))
_const.CASEFILEPATH = path + "/cases/"
_const.LOGPATH = path + "/logs/"
_const.RESULTS = path + "/allure-results/"
