#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-15 下午4:36
# @Author : Liuchuan
# @File   : simple_import_price.py.py
import pandas as pd
import numpy as np
import datetime
import config
import wcsv

filename = 'product-info-config-filter-' + str(datetime.date.today()) + '.csv'
filepath = config.get_file_path(filename, 'csv')

df = pd.read_csv(filepath)
df = df.replace(np.nan, '', regex=True)

simples = []
for i in df.index.values:
    row = df.ix[i].to_dict()
    p_sku = row['p_sku']
    children = [int(x) for x in row['children'].split('|') if x != '']
    if p_sku == '' or len(children) <= 0:
        continue
    skus = {
        '5mm Non Faux Teak': int(row['5mm Non Faux Teak']),
        '6mm Non faux Teak': int(row['6mm Non faux Teak']),
        '6mm Faux Teak': int(row['6mm Faux Teak'])
    }

    for k,s in skus.items():
        if s in children:
            item = {'sku': s}
            if k == '5mm Non Faux Teak':
                price = row['5mm Non-Faux Teak Price'].replace('$', '').replace(',', '').strip()
            elif k == '6mm Non faux Teak':
                price = row['6mm Non-Faux Teak Price'].replace('$', '').replace(',', '').strip()
            elif k == '6mm Faux Teak':
                price = row['6mm Faux Teak Price'].replace('$', '').replace(',', '').strip()
            else:
                price = 0
            item['price'] = price
            simples.append(item)

header = ['sku', 'price']
if len(simples) > 0:
    wcsv.data_write(header, simples, 'import-simple-product-price-file')

