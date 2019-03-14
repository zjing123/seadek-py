#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-13 下午3:40
# @Author : Liuchuan
# @File   : parse.py

from os import path
import panda
import wcsv
import datadump
import re

filename = path.dirname(path.abspath(__file__)) + '/product-info.csv'

data = panda.get_file_data(filename, 'csv')
skus = panda.get_all_sku(filename, 'csv')

db_data = datadump.get_product()

product_skus = []
for i in db_data:
    product_skus.append(i[0])

not_contain_sku = []
for i in skus:
    if i not in product_skus:
        print(i)
        not_contain_sku.append(i)

products = []
no_exists_products = []
for i in data:
    # re.sub(pattern, '127.0.0.1', url)
    # pattern = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    skus = list(map(lambda x:x.strip(), i[1:4]))

    prices = list(map(lambda x:x.replace('$', '').replace(',', '').strip(), i[4:7]))

    for k in range(0,len(skus)):
        prod = {
                'sku': skus[k],
                'price': prices[k]
            }
        if skus[k] in not_contain_sku:
            no_exists_products.append(prod)
        else:
            products.append(prod)


header = ['sku', 'price']
if len(products) > 0:
    wcsv.data_write(header, products, 'product')

if len(no_exists_products) > 0:
    wcsv.data_write(header, no_exists_products, 'product-not-exists')

# print(products)
# wcsv.data_write(header, products, 'product-in-sku')
