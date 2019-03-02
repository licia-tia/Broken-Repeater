# -*- coding: utf-8 -*-
import requests
import re
from multiprocessing import Pool
import json


def test():
    URL = 'https://zh.wiktionary.org/zh/'
    f = open('字表', 'r', encoding='UTF-8')
    result = {}
    c = 0
    # pat = '系列#\w+（<span style="font-size:160%"><b><a class="mw-selflink selflink">(.)</a></b></span>）：'
    pat = '系列#\w+（<span style="font-size:160%"><b><a href="/wiki/.+" title=".">(.)</a></b></span>）'
    for char in f.read():
        try:
            # c += 1
            # if c < 3000:
            #     continue
            # elif c > 3010:
            #     break
            r = requests.get(URL + char)
            sub = re.search(pat, r.text).group(0)[-17]
            print(char, sub)
            result.setdefault(char, sub)
        except:
            pass

    print(result)


def search(_char):
    try:
        url = 'https://zh.wiktionary.org/zh/' + _char
        r = requests.get(url)
        sub = re.search('系列#\w+（<span style="font-size:160%"><b><a href="/wiki/.+" title=".">(.)</a></b></span>）',
                        r.text).group(0)[-17]
        return sub
    except:
        return _char


if __name__ == '__main__':
    f = open('字表', 'r', encoding='UTF-8')
    file = f.read()
    # file = '鸟儿抬头望着远处的一湾泉水回答现在我爱那一湾泉水我有点渴了'
    searched = {}
    pool = Pool(processes=128)

    for char in file:
        searched.setdefault(char, pool.apply_async(search, args=(char,)))
    pool.close()
    pool.join()

    result = {}
    for i in searched:
        result.setdefault(i, searched.get(i).get())

    jsObj = json.dumps(result)
    fileObject = open('data.json', 'w')
    fileObject.write(jsObj)
    fileObject.close()

