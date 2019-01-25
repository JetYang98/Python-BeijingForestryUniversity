# 网页提交内容到服务器，是以链接形式传输的，第8、9行结果相同

import requests

keyword = "Python"
try:
    kv = {'wd': keyword}    # 查询关键字的接口 ， 360用的是 q 
    # r = requests.get("http://www.baidu.com/s", params=kv)
    r = requests.get('http://www.baidu.com/s?wd=Python')    # 和上一行相同
    print(r.request.url)    # 接口形式： http://www.baidu.com/s?wd=Python
    r.raise_for_status()
    print(len(r.text))
except:
    pirnt('爬取失败')