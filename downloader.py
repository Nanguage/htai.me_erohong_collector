#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import configer

def download(info):

    prefs = {"download.default_directory" : configer.download_path}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(chrome_options=chrome_options)

    for item in info:
        print(item['link'] + item['title'])
        try:
            if 'yunpan' in item['link']:
                browser.get(item['link'])
                element = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'pwd-input')))
                pw_ele = browser.find_element_by_class_name('pwd-input')
                pw_ele.send_keys(item['password'])
                element = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'submit-btn')))
                clc_ele = browser.find_element_by_class_name('submit-btn')
                clc_ele.click()
                element = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.ID, 'download')))
                dwn_ele = browser.find_element_by_id('download')
                dwn_ele.click()
                time.sleep(2)
        except Exception as e:
            print(str(e))
    
    print("waiting for download!")
    time.sleep(20)
    total_time = 20
    while True:
        file_list = os.listdir(configer.download_path)
        flag = False
        for f in file_list:
            if f.endswith('crdownload'):
                flag = True
                break
        if flag == False:
            break
        if total_time > configer.download_time_limit:
            print("wating too long!")
            break
        total_time += 10
        print("total time + 10s : %ss"%(total_time))
        time.sleep(10)
    browser.close()
