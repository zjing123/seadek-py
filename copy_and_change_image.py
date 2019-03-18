#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-18 下午2:45
# @Author : Liuchuan
# @File   : copy_and_change_image.py
import shutil
import os


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
            os.rmdir(c_path)
        else:
            os.remove(c_path)


def change_file_name(path):
    ls = os.listdir(path)
    for i in ls:
        old_path = os.path.join(path, i)
        new_name = '-'.join([x.strip('-').replace(',', '') for x in i.split(' ') if x != '-'])
        new_path = os.path.join(path, new_name)
        # print(old_path, new_path)
        os.rename(old_path, new_path)
