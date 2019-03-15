#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-15 上午10:01
# @Author : Liuchuan
# @File   : config.py
from os import path

ROOT = path.dirname(path.abspath(__file__))


def get_file_path(filename, type="var"):
    if type == 'var':
        return ROOT + '/var/' + filename
    else:
        return ROOT + '/Csv/' + filename
