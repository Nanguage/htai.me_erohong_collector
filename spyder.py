#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from urllib.request import urlopen
from multiprocessing import Pool

from bs4 import BeautifulSoup

import configer

root_url = configer.main_page
#headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}

def get_pages_url():
    pages = [(root_url +"page/%d"%i) for i in range(configer.start_page, configer.end_page + 1)]
    return pages

def get_urls():
    articles_url = []
    pages_url = get_pages_url()
    p = Pool(configer.cpu_core)
    asy_results = []
    for page in pages_url:
        #print(page)
        asy_results.append(
                p.apply_async(get_articles, kwds={'url':page})
                )
    p.close()
    p.join()
    for r in asy_results:
        for url in r.get():
            articles_url.append(url)
            #print(url)
    #articles_url.sort()
    return articles_url[1:]

def get_articles(url):
    try:
        html = urlopen(url, timeout=configer.download_time_limit).read()
    except Exception as e:
        print(e)
    soup = BeautifulSoup(html, 'html.parser' )
    page_articles_url = []
    arti_node = soup.find_all('article', class_='article clearfix')
    for i in arti_node:
        page_articles_url.append(i.find('a').attrs['href'])
    #print(os.getpid())
    return page_articles_url

def get_infos(urls):
    infos = []
    p = Pool(configer.cpu_core)
    asy_results = []
    for url in urls:
        asy_results.append(
                p.apply_async(get_page_info, kwds={'url':url})
                )
    p.close()
    p.join()
    for r in asy_results:
        info = r.get()
        if info != {}:
            infos.append(r.get())
    return infos

def get_page_info(url):
    try:
        html = urlopen(url, timeout=configer.parse_timeout).read()
        soup  = BeautifulSoup(html, 'html.parser')
        file_name = soup.find_all('p')[2].get_text().split('，')[0]
        if not file_name.startswith('[Htai.me]'):
            raise IsNotHongException
        title = soup.find('h1', id='post_title').get_text().replace(',', '')
        title = title.replace('\n', '')[:100]
        table = soup.find('table')
        link  = table.find('a').attrs['href']
        trs   = table.find_all('tr')
        tr2   = trs[1]
        td1   = tr2.find('td')
        td2   = td1.find_next_sibling()
        pw    = td2.get_text()
        print(url)
        print(title)
        info = {'title':title, 'link':link, 'password':pw, 'file_name':file_name}
    except Exception as e:
        info = {}
        print(e)
    return info


class IsNotHongException(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return "Maybe, it's not hong ~_~"

        
