#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: KyleYeung
# datetime:2022/8/8 17:27
# software: PyCharm

import logging
from logging.handlers import RotatingFileHandler  # 按文件大小滚动备份
import time
import os
import const


class Log(object):
    def __init__(self, logger):
        # 创建一个handler，用于写入日志文件
        rq = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # log_path = os.getcwd() + "/result/logs/"
        log_path = const.LOGPATH

        # 文件不存在时，创建文件
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_name = log_path + rq + '_' + ".log"

        self.log_name = log_name
        self.logger = logging.getLogger(name=logger)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter("%(asctime)s %(name)s:%(levelname)s:%(message)s")  # 日志输出格式

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = RotatingFileHandler(filename=self.log_name, mode='a', maxBytes=1024 * 1024 * 5, backupCount=5,
                                 encoding='utf-8')  # 使用RotatingFileHandler类，滚动备份日志
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'exception':
            self.logger.exception(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()  # 关闭打开的文件

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def exception(self, message):
        self.__console('exception', message)
