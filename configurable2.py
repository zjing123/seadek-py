#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-15 下午5:40
# @Author : Liuchuan
# @File   : configurable2.py
import pandas as pd
import numpy as np
import datetime
import config
import re
import wcsv

filename = 'catalog_product_20190315_063059.csv'
filepath = config.get_file_path(filename)

df = pd.read_csv(filepath)
df = df.replace(np.nan, '', regex=True)
skus = []
for i in df.index.values:
    item = df.ix[i].to_dict()
    skus.append(item['sku'].strip())

filename = 'product-info-config-' + str(datetime.date.today()) + '.csv'
filepath = config.get_file_path(filename, 'csv')


def has_skus(data, skux):
    # print(skux)
    has_sku = []
    sku_5mm = data['5mm Non Faux Teak']
    sku_6mm = data['6mm Non faux Teak']
    sku_6mm_teak = data['6mm Faux Teak']
    if sku_5mm and str(int(sku_5mm)).strip() in skux:
        has_sku.append(int(sku_5mm))
    if sku_6mm and str(int(sku_6mm)).strip() in skux:
        has_sku.append(int(sku_6mm))
    if sku_6mm_teak and str(int(sku_6mm_teak)).strip() in skux:
        has_sku.append(int(sku_6mm_teak))

    return ' | '.join([str(x) for x in has_sku])


df = pd.read_csv(filepath)
df = df.replace(np.nan, '', regex=True)
items = []
for i in df.index.values:
    row = df.ix[i].to_dict()
    if row['5mm Non Faux Teak'] and row['6mm Non faux Teak'] and row['6mm Faux Teak']:
        row['sku_exists'] = has_skus(row, skus)
    items.append(row)

header = [
    'name',	'5mm Non Faux Teak', '6mm Non faux Teak', '6mm Faux Teak',
    '5mm Non-Faux Teak Price', '6mm Non-Faux Teak Price', '6mm Faux Teak Price',
    'p_sku', 'p_name', 'children', 'sku_exists'
]

if len(items) > 0:
    wcsv.data_write(header, items, 'product-info-config-sku-exists')
