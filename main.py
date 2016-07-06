#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import passwd
import configer
import downloader
import name_changer
from spyder import get_urls, get_pages_url, get_infos

def out_csv(info):
    with open('result.csv', 'w') as f:
        for i in info:
            s = "%s,%s,%s,%s"%(i['link'], i['password'], i['title'], i['file_name'])
            print(s, file=f)

if __name__ == '__main__':
    print("parsing page...")
    urls = get_urls()
    print(urls)
    infos = get_infos(urls)
    print(infos)
    out_csv(infos)
    print(infos)
    print("PARSE DONE!")
    downloader.download(infos)
    print("DOWNLOAD DONE!")
    name_changer.change()
    print("NAME CHANGED!")
    passwd.run()
    print("DONE!")

