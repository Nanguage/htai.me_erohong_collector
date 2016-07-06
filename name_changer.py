#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv

import configer
import datetime

def change():
    change_dict = {}
    reader = csv.reader(open('./result.csv'))
    for l, p, title, file_name in reader:
        change_dict[file_name + '.zip'] = title
    
    PATH = configer.download_path
    file_list = os.listdir(PATH)
    today = datetime.datetime.now().strftime("%m-%d")
    i = 0
    for f in file_list:
        if f in change_dict:
            i += 1
            index = i if len(str(i)) > 1 else "0%s"%str(i)
            new_name = "[%s][%s]%s.zip"%(today, index, change_dict[f][:configer.name_length_limit])
            os.rename(PATH + f, PATH + new_name)

if __name__ == '__main__':
    change()
