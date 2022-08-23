#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: KyleYeung
# datetime:2022/8/8 17:27
# software: PyCharm

import yaml


class ReadYaml(object):
    def __init__(self, config_path):
        self.config_path = config_path
        with open(self.config_path, 'r', encoding='UTF-8') as f:
            self.data = yaml.safe_load(f)

    def get_base_info(self, name):
        value = self.data['base_info'][name]
        return value

    def get_user_info(self, name):
        value = self.data['user_info'][name]
        return value

