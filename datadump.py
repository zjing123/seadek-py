#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-14 下午3:10
# @Author : Liuchuan
# @File   : datadump.py
import pymysql

HOST = 'localhost'
USER = 'liuchuan'
PASS = 'liuchuan'
DB = 'magento2_seadek_dev'

# 打开数据库连接
db = pymysql.connect(HOST, USER, PASS, DB)

# 使用cursor()方法获取操作游标
cursor = db.cursor()


def get_connect(host, username, password, dbname):
    return pymysql.connect(host, username, password, dbname)


def get_product(sql="select sku from catalog_product_entity where type_id = 'simple'"):
    connect = get_connect(HOST, USER, PASS, DB)
    cursor = connect.cursor()
    results = []

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except:
        print('Error: unable to fetch data')

    # 关闭数据库连接
    connect.close()
    return results


# # SQL 查询语句
# sql = "select sku from catalog_product_entity where type_id = 'simple'"
#
# print(get_product(sql))
