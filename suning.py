#coding=utf-8
import re
from bs4 import BeautifulSoup
from common import open_url_str, open_url_json, parse_json_like_str

main_url='http://www.suning.com/webapp/wcs/stores/ItemPrice/%s__9315_12502_1.html'

def get_price(url):
    content = open_url_str(url)
    soup = BeautifulSoup(content)
    name = soup.find(id = "ga_itemDataBean_description_name").get('value')
    part_num = soup.find(id = "curPartNumber").get('value')
    content = open_url_str(main_url%(part_num))
    factory_send_flag = parse_json_like_str('factorySendFlag',content)
    price = parse_json_like_str('netPrice',content)
    if (factory_send_flag != ''):
        return name, price
    else:
        return name, None