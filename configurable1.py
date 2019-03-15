#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-15 下午2:41
# @Author : Liuchuan
# @File   : configurable1.py
import pandas as pd
import numpy as np
import panda
import config
import re
import wcsv

filename = 'simple-config-prod.csv-2019-03-15.csv'
filepath = config.get_file_path(filename)

df = pd.read_csv(filepath)

items = dict()
for i in df.index.values:
    item = df.ix[i].to_dict()
    p_name = item['p_name'].replace('"', '').strip()
    if p_name in items:
        items[p_name]['children'] += ' | ' + str(item['sku'])
    else:
        items[p_name] = {
            'p_sku': item['p_sku'],
            'p_name': p_name,
            'children': str(item['sku'])
        }

# filename1 = 'catalog_product_20190315_063059.csv'
# filepath1 = config.get_file_path(filename1)
#
#
# exit()

filepath = config.get_file_path('product-info1.csv')
df = pd.read_csv(filepath)
df = df.replace(np.nan, '', regex=True)

p_datas = []
p_datas_filter = []
for i in df.index.values:
    dt = df.ix[i].to_dict()
    name = dt['name'].replace('"','').strip()
    if 'Unnamed: 7' in dt:
        dt.pop('Unnamed: 7')
    if name in items and dt['5mm Non Faux Teak'] != '':
        dt['p_sku'] = items[dt['name']]['p_sku']
        dt['p_name'] = items[dt['name']]['p_name']
        dt['children'] = items[dt['name']]['children']
    if dt['5mm Non Faux Teak'] != '':
        p_datas_filter.append(dt)

    p_datas.append(dt)

header = [
    'name',	'5mm Non Faux Teak', '6mm Non faux Teak', '6mm Faux Teak',
    '5mm Non-Faux Teak Price', '6mm Non-Faux Teak Price', '6mm Faux Teak Price',
    'p_sku', 'p_name', 'children'
]

if len(p_datas) > 0:
    wcsv.data_write(header, p_datas, 'product-info-config')

if len(p_datas_filter) > 0:
    wcsv.data_write(header, p_datas_filter, 'product-info-config-filter')
