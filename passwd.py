#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os

import configer

PATH = configer.download_path
pw   = configer.zip_passwd

def run():
    os.chdir(PATH)
    os.mkdir(PATH + "cache")
    cache_path = PATH + 'cache/'
    file_list = [i for i in filter(lambda s:s.endswith('.zip') ,os.listdir(PATH))]
    for f in file_list:
        print("[UNZIP]")
        subprocess.call(["unzip", "-P", pw, "-d", cache_path, PATH + f])
        print("[ZIP]")
        #subprocess.call(["zip", "-r", f, cache_path + '*'])
        os.system("rm %s"%('"'+f+'"'))
        os.system("zip -o -r -j %s %s"%('"'+f+'"', './cache/*'))
        print("[CLEAN]")
        #subprocess.call(["rm", "-r", cache_path + '*'])
        os.system("rm -r %s"%(cache_path+'*'))
    subprocess.call(["rm", "-r", cache_path])

if __name__ == '__main__':
    run()
