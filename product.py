#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-14 上午9:51
# @Author : Liuchuan
# @File   : product.py

THICKNESS = ["5mm", "6mm", "6mm"]
TEAK_STYLE= ['Non-Faux Teak', 'Non-Faux Teak', 'Faux Teak']
THICKNESS_TEAK_STYLE = ['5mm-Non-Faux-Teak', '6mm-Non-Faux-Teak', '6mm-Faux-Teak']
HEADER = [
    'sku', 'attribute_set_code', 'product_type', 'categories',
    'product_websites', 'name', 'visibility', 'price', 'url_key',
    'qty', 'out_of_stock_qty', 'configurable_variations', 'configurable_variation_labels'
]

HEADER_KAYAK = ['sku', 'price', 'description']


def get_product(type='simple'):
    if type == 'simple':
        return {
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
    else:
        return {
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
