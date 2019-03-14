#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-14 上午9:31
# @Author : Liuchuan
# @File   : files.py

import os


def create__file(filepath):
    (file_path, file_name) = os.path.split(filepath)
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    if has_csv(filepath) is False:
        os.mknod(filepath)


def has_csv(filepath):
    return os.path.exists(filepath)
