import requests

url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
try:
    kv = {"user-agent": "Mozilla/5.0"}  # 当作谷歌浏览器访问亚马逊，否则访问失败
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:100])
except:
    print("爬取失败")