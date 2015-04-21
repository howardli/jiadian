#coding=utf-8
import sys, codecs, os
from urlparse import urlparse
from gome import get_price as get_gome_price
from suning import get_price as get_suning_price
from jd import get_price as get_jd_price

file_path = os.path.normpath(os.path.dirname(__file__))

def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    param_file = codecs.open(os.path.join(file_path, 'param'), 'r', 'utf-8')
    params = param_file.readlines()
    param_file.close()
    for param in params:
        p = param.strip('\r\n').split(',')
        min_price = p[0]
        url = p[1]
        open(min_price, url)

def open(min_price,url):
    while True:
        try:
            shop, name , price = '', '', ''
            if 'gome' in urlparse(url).hostname:
                shop = '国美'
                name , price = get_gome_price(url)
            elif 'suning' in urlparse(url).hostname:
                shop = '苏宁'
                name , price = get_suning_price(url)
            elif 'jd' in urlparse(url).hostname:
                shop = '京东'
                name , price = get_jd_price(url)
            if not price:
                print '%s，%s无货'%(shop,name)
            else:
                print '%s，%s现在价格是%s，地址是%s'%(shop, name, price, url)
            break
        except Exception, e:
            pass

if __name__ == '__main__':
    main()