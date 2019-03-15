#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-13 下午3:40
# @Author : Liuchuan
# @File   : parse1.py

from os import path
import panda
import wcsv
import datadump
import product
import config

HEADER = ['sku', 'price', 'description']

filename = config.PATH['product-kayak-csv']
data = panda.get_file_data(filename, 'csv')

skus = []
for d in data:
    skus.extend(list(map(lambda k:int(k), d[0:2])))

db_data = datadump.get_product()

product_skus = []
for i in db_data:
    product_skus.append(i[0])

not_contain_sku = []
for i in skus:
    if i not in product_skus:
        not_contain_sku.append(i)

# print(not_contain_sku)
products = []
no_exists_products = []
for i in data:
    for k in list(map(lambda m:int(m), i[0:2])):
        prod = {
            'sku': k,
            'price': i[3],
            'description': i[2]
        }
        if k in not_contain_sku:
            no_exists_products.append(prod)
        else:
            products.append(prod)


if len(products) > 0:
    wcsv.data_write(product.HEADER_KAYAK, products, 'product-kayak')

if len(no_exists_products) > 0:
    wcsv.data_write(product.HEADER_KAYAK, no_exists_products, 'product-kayak-not-exists')
