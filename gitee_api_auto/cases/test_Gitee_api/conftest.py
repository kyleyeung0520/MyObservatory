#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: KyleYeung
# datetime:2022/8/8 17:27
# software: PyCharm

import pytest
import os
from tools.read_yaml import ReadYaml


client = None

@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir,
                               "config",
                               request.config.getoption('environment'),
                               "config_ct.yaml")
    config = ReadYaml(config_path)

    return config




