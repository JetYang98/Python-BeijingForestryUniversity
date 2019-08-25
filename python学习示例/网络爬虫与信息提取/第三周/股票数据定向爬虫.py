import requests 
from bs4 import BeautifulSoup
import traceback, re

def get_HTML_text(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        # print(r.text)
        return r.text
    except:
        return ""

def get_stock_list(lst, stock_url):
    html = get_HTML_text(stock_url, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    # print(type(soup))
    a = soup.find_all('a')
    for i in a:
        # print(type(i))
        try:
            href = i.attrs["href"]
            temp = re.findall(r'[s][hz]\d{6}', href)[0]
            # print(temp)
            lst.append(temp)
        except:
            continue

def get_stock_info(lst, stock_url, fpath):
    count = 0
    for stock in lst:
        url = stock_url + stock + '.html'
        html = get_HTML_text(url)
        try:
            if html == '':
                continue
            info_dict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stock_info = soup.find('div', attrs={'class': "stock-bets"})
            name = stock_info.find_all(attrs={'class': 'bets-name'})[0]
            info_dict.update({'股票名称': name.text.split()[0]})
            key_list = stock_info.find_all('dt')
            value_list = stock_info.find_all('dd')
            for i in range(len(key_list)):
                key = key_list[i].text
                val = value_list[i].text
                info_dict[key] = val
            print(info_dict)
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(info_dict) + '\n')
                count = count + 1
                print('\r当前进度：{:.2f}%'.format(count*100/len(lst)), end='')
        except:
            count = count + 1
            print('\r当前进度：{:.2f}%'.format(count*100/len(lst)), end='')

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D:/BaiduStockInfo.txt'
    slist = []
    get_stock_list(slist, stock_list_url)
    get_stock_info(slist, stock_info_url, output_file)

main()
