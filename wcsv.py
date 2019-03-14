#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-14 上午9:19
# @Author : Liuchuan
# @File   : wcsv.py

import csv
from os import path
import datetime
import files


def data_write(headers, data, filename='products'):
    dir_path = path.dirname(path.abspath(__file__)) + '/Csv/'
    file_path = dir_path + filename + '-' + str(datetime.date.today()) + '.csv'

    if files.has_csv(file_path) is False:
        files.create__file(file_path)

    csv_file = open(file_path, 'w')
    dict_writer = csv.DictWriter(csv_file, headers)
    dict_writer.writeheader()
    dict_writer.writerows(data)

    csv_file.close()
