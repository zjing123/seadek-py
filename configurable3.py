#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-18 下午2:40
# @Author : Liuchuan
# @File   : configurable3.py
import pandas as pd
import numpy as np
import shutil
import os
import config
import wcsv
import copy_and_change_image as caci

def get_image_list(filepath):
    ls = os.listdir(filepath)
    images = {}
    for i in ls:
        split = os.path.splitext(i)
        name = '-'.join(split[0].split('-')[0:-1]).strip()
        filename = '-'.join([x.strip('-').replace(',', '') for x in i.split(' ') if x != '-'])
        # print([x.strip('-') for x in i.split(' ') if x != '-'])
        # print(filename)
        if name in images:
            images[name].append(filename)
        else:
            images[name] = [filename]
    return images


def parse_file_data(filepath, images):
    df = pd.read_csv(filepath)
    df = df.replace(np.nan, '', regex=True)
    items = []
    for i in df.index.values:
        row = df.ix[i].to_dict()
        nm = row['name']
        item = {
            'name': row['name'],
            'sku': row['p_sku']
        }

        if nm in images:
            img_num = 1
            for k in images[nm]:
                item['img' + str(img_num)] = k
                img_num = img_num + 1
        items.append(item)
    return items


def copy_images_and_change_name(oldpath, newpath):
    # 复制文件
    if os.path.exists(newpath):
        caci.del_file(newpath)
        os.rmdir(newpath)
    shutil.copytree(oldpath, newpath)
    # 更改文件名
    caci.change_file_name(newpath)


filepath = '/media/liuchuan/LENOVO/work/Files/Seadek/Files/Products/0318/SeaDekimage/image'
images = get_image_list(filepath)

filename = 'product-info-config-filter-2019-03-15.csv'
filepath = config.get_file_path(filename, 'csv')
items = parse_file_data(filepath, images)

# for i in items:
#     name = i['name'].strip()
#     if name in images:
#         images[name].append(1)
#
# for i in images.items():
#     print(i)


header = ['name','sku', 'img1', 'img2']
if len(items) > 0:
    wcsv.data_write(header, items, 'congifurable_product_image')

filepath = '/media/liuchuan/LENOVO/work/Files/Seadek/Files/Products/0318/SeaDekimage/image'
filepath1 = '/media/liuchuan/LENOVO/work/Files/Seadek/Files/Products/0318/SeaDekimage/new_image'
copy_images_and_change_name(filepath, filepath1)
