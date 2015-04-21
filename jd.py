#coding=utf-8
import re
from bs4 import BeautifulSoup
from common import open_url_str, open_url_json, parse_json_like_str

price_url = 'http://p.3.cn/prices/get?skuid=J_%s&type=1&area=15_1213_3410'
status_url = 'http://st.3.cn/gds.html?skuid=%s&provinceid=15&cityid=1213&areaid=3410&townid=0'

def get_price(url):
    content = open_url_str(url)
    soup = BeautifulSoup(content)
    name = soup.findAll("div", {"class" : "p-name"})[0].string
    r = re.compile('pageConfig = ')
    for script in soup.find_all("script", {"src":False}):
        s = r.search(script.string)
        if s:
            skuid = parse_json_like_str('skuid',script.string)
            skuidkey = parse_json_like_str('skuidkey',script.string)
            if get_status(skuidkey)=='有货':
                return name, get_price_key(skuid)
            else:
                return name, None

def get_price_key(skuidkey):
    url = price_url%(skuidkey)
    json = open_url_json(url)
    return json[0]['p']

def get_status(skuid):
    url = status_url%(skuid)
    json = open_url_json(url)
    return json['stock']['StockStateName']