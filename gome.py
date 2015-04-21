#coding=utf-8
import re
from bs4 import BeautifulSoup
from common import open_url_str, open_url_json, parse_json_like_str

main_url='http://g.gome.com.cn/ec/homeus/browse/store.jsp?goodsNo=%s&city=22010500&areaId=220105009&siteId_p=%s&skuType_p=%s&shelfCtgy3=%s&zoneId=22010000&sid=%s&pid=%s&programId=%s'
limitbuy_groupon_url='http://www.gome.com.cn/ec/homeus/n/product/browse/getProductLimitbuyAndGrouponJsonData.jsp?productId=%s&skuId=%s'

def get_price(url):
    content = open_url_str(url)
    soup = BeautifulSoup(content)
    r = re.compile('prdInfo = ')
    for script in soup.find_all("script", {"src":False}):    
        s = r.search(script.string)
        if s:
            sku_no = parse_json_like_str('skuNo',script.string)
            site_id = parse_json_like_str('siteId',script.string)
            sku_type = parse_json_like_str('skuType',script.string)
            shelf = parse_json_like_str('shelf',script.string)
            sku = parse_json_like_str('sku',script.string)
            prd_id = parse_json_like_str('prdId',script.string)
            program_id = parse_json_like_str('programId',script.string)
            description = parse_json_like_str('description',script.string)
            url = main_url%(sku_no, site_id, sku_type, shelf, sku, prd_id, program_id)
            json = open_url_json(url)
            price1 = json['price']
            result1 = json['result']
            price2 = get_limitbuy_groupon_price(prd_id ,sku)
            if (result1 == 'Y'):
                if (price2 != ''):
                    return description, price2
                else:
                    return description, price1
            else:
                return description, None

def get_limitbuy_groupon_price(productId, skuId):
    url = limitbuy_groupon_url%(productId,skuId)
    json = open_url_json(url)
    return json['price']