#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-13 下午4:12
# @Author : Liuchuan
# @File   : panda.py
from os import path
import numpy as np
import pandas as pd

MAX_ROW = 272
MAX_COL = 10

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
    if len(data) <= 1:
        continue
    datas.append(data)

# print(header)
simple = {
    'sku': '',
    'attribute_set_code': 'Default',
    'product_type': 'simple',
    'categories': 'Default Category/Test Category',
    'product_websites': 'base',
    'name': '',
    'visibility': 'Not Visible Individually',
    'price': 0,
    'url_key': '',
    'qty': 999,
    'out_of_stock_qty': 0,
    'configurable_variations': '',
    'configurable_variation_labels': ''
}

configurable = {
    'sku': '',
    'attribute_set_code': 'Default',
    'product_type': 'configurable',
    'categories': 'Default Category/Test Category',
    'product_websites': 'base',
    'name': '',
    'visibility': 'Catalog, Search',
    'price': '',
    'url_key': '',
    'qty': 0,
    'out_of_stock_qty': 0,
    'configurable_variations': '',
    'configurable_variation_labels': 'thickness=Thickness,teak_style=teak style'
}

products = []
thickness = ["5mm", "6mm", "6mm"]
teak_style= ['Non-Faux-Teak', 'Non-Faux-Teak', 'Faux-Teak']
thickness_teak_style = ['5mm-Non-Faux-Teak', '6mm-Non-Faux-Teak', '6mm-Faux-Teak']

sku_num = 1
for data in datas:
    skus = str(data[1]).split('|')
    config_prod = configurable
    name = data[0]
    config_prod['sku'] = 'col-' + str(sku_num)
    config_prod['name'] = name
    config_prod['url_key'] = (config_prod['sku'] + '-' + name.replace(' ', '-')).lower()
    sku_num = sku_num + 1

    print(skus)
    simples = []
    for i in skus:
        print(i)
        index = skus.index(i)
        sku, thick, teak, tts = i.strip(), thickness[index], teak_style[index], thickness_teak_style[index]
        # print(sku)
        prod = simple
        prod['sku'] = sku
        prod['name'] = '{}-{}'.format(name.replace(' ', '-'), tts)
        prod['url_key'] = '{}-{}'.format(prod['name'], prod['sku']).lower()
        configurable_variations = 'sku={},thickness={},teak_style={}' .format(sku, thick, teak)
        if config_prod['configurable_variations'] == '':
            config_prod['configurable_variations'] = configurable_variations
        else:
            config_prod['configurable_variations'] += '|' + configurable_variations
        print(prod)
        products.append(prod)
    products.append(config_prod)
    print(products)
    break


# https://www.cnblogs.com/liulinghua90/p/9935642.html
# https://www.cnblogs.com/lingzeng86/p/6793398.html
# https://www.cnblogs.com/shaosks/p/6098282.html
