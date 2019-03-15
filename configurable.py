#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-15 上午9:57
# @Author : Liuchuan
# @File   : configurable.py

import pandas as pd
import numpy as np
import panda
import config
import re
import wcsv
import datadump

filename = 'product-2019-03-14.csv'
filepath = config.get_file_path(filename)

datas = panda.get_file_data(filepath, 'csv')
datas = [str(int(k[0])) for k in datas]
print(datas)

filename1 = 'catalog_product_20190315_063059.csv'
filepath1 = config.get_file_path(filename1)

df = pd.read_csv(filepath1)
df = df.replace(np.nan, '', regex=True)
items = []
for i in df.index.values:
    item = df.ix[i].to_dict()
    if item['product_type'] == 'configurable'\
       and item['configurable_variations'] != '':
        items.append(df.ix[i].to_dict())

f_items = []
for i in items:
    f_item = {
        'sku': i['sku'],
        'name': i['name'],
        'configurable_variations': i['configurable_variations']
    }
    f_items.append(f_item)    # print(i['configurable_variations'])



# for i in f_items:
#     # print(i['configurable_variations'])
#     configurable_var = i['configurable_variations']
#     match = re.findall(r'sku=(.*?),', configurable_var)
#     # print(match)
#
#     break

f_items = list(map(lambda x: ({
    'sku': x['sku'],
    'name': x['name'],
    'children': re.findall(r'sku=(.*?),', x['configurable_variations'])
}), f_items))

p_items = []
for i in f_items:
    children = i['children']
    if len(children) > 0:
        for k in children:
            if k in datas:
                p_item = {
                    'sku': k,
                    'p_sku': i['sku'],
                    'p_name': i['name']
                }
                p_items.append(p_item)

# print(p_item)

print(p_items)
p_items = sorted(p_items,key = lambda x:x['sku'])

print(p_items)

for k in p_items:
    print(k)

header = ['sku', 'p_sku', 'p_name']
wcsv.data_write(header, p_items, 'simple-config-prod.csv')
