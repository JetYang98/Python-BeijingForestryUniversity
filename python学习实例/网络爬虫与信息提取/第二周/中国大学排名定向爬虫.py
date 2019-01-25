import requests
from bs4 import BeautifulSoup
import bs4

def get_HTML_text(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fill_univ_list(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')  # 查找所有的td标签 等价于 tr.find_all('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

# def print_univ_list(ulist, num):
#     print("{:^10}\t{:^10}\t{:^10}".format("排名","学校名称","总分"))
#     for i in range(num):
#         u = ulist[i]
#         print("{:^10}\t{:^10}\t{:^10}".format(u[0],u[1],u[2]))

###############################################################
# 改进的函数
def print_univ_list(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288))) # chr(12288)是中文空格，解决中英文空格不对齐问题
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = get_HTML_text(url)
    fill_univ_list(uinfo, html)
    print_univ_list(uinfo, 20)  # 打印20所大学

main()