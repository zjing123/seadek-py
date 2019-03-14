#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-13 下午4:12
# @Author : Liuchuan
# @File   : panda.py
from os import path
import numpy as np
import pandas as pd
import pprint
import product
import wcsv


def get_file_data(filename, type='excel'):
    df = None
    if type == 'excel':
        df = pd.read_excel(filename)
    elif type == 'csv':
        df = pd.read_csv(filename)
    if df is None:
        return None
    df = df.replace(np.nan, '', regex=True)
    items = []
    for i in df.index.values:
        if i == 0:
            continue
        row_data = df.ix[i].to_list()
        item = [k for k in row_data if k not in ['', ' ', 'nan']]
        if len(item) <= 2:
            continue
        items.append(item)
    return items


def get_all_sku(filename, type='excel'):
    skus = []
    datas = get_file_data(filename, type)
    for data in datas:
        skus.extend(data[1:4])
    return skus


# filename = path.dirname(path.abspath(__file__)) + '/product-info.csv'
# datas = get_all_sku(filename, 'csv')
#
# products = []


# print(get_file_data(filename, 'csv'))

'''
print(123)
filename = path.dirname(path.abspath(__file__)) + '/product-info.xlsx'
df = pd.read_excel(filename)
df = df.replace(np.nan, '', regex=True)

header = df.ix[0].to_list()
datas = []
for i in df.index.values:
    if i == 0:
        continue
    row_data = df.ix[i].to_list()
    data = [i for i in row_data if i not in ['', ' ', 'nan']]
    if len(data) <= 2:
        continue
    datas.append(data)


products = []
sku_num = 1
for data in datas:
    skus = str(data[1]).split('|')
    config_prod = product.get_product('configurable')
    name = data[0]
    config_prod['sku'] = 'col-' + str(sku_num)
    config_prod['name'] = name
    config_prod['url_key'] = (config_prod['sku'] + '-' + name.replace(' ', '-')).lower()
    sku_num = sku_num + 1

    simples = []
    num = 1
    for i in skus:
        index = skus.index(i)
        num = num + 1
        sku, thick, teak, tts = i.strip(), product.THICKNESS[index], product.TEAK_STYLE[index], product.THICKNESS_TEAK_STYLE[index]

        prod = product.get_product()
        prod['sku'] = sku
        prod['name'] = '{}-{}'.format(name.replace(' ', '-'), tts)
        prod['url_key'] = '{}-{}'.format(prod['name'], prod['sku']).lower()
        prod['price'] = data[num]
        configurable_variations = 'sku={},thickness={},teak_style={}' .format(sku, thick, teak)
        if config_prod['configurable_variations'] == '':
            config_prod['configurable_variations'] = configurable_variations
        else:
            config_prod['configurable_variations'] += '|' + configurable_variations
        products.append(prod)
    products.append(config_prod)

if len(products) > 0:
  wcsv.data_write(product.HEADER, products)
'''
# https://www.cnblogs.com/liulinghua90/p/9935642.html
# https://www.cnblogs.com/lingzeng86/p/6793398.html
# https://www.cnblogs.com/shaosks/p/6098282.html
