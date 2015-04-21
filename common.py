#coding=utf-8
import urllib3, json, re, chardet

def open_url_str(url):
    http = urllib3.PoolManager()
    request = http.request('GET', url)
    return request.data

def open_url_json(url):
    str = open_url_str(url)
    return json.loads(str.decode(chardet.detect(str)['encoding']))

def parse_json_like_str(param_name, string):
    r = re.compile(param_name+'(.*?):(.*?)[,}]')
    m = r.search(string)
    return m.group(2).replace('"','').replace('\'','').replace(' ','')

if __name__ == '__main__':
    print parse_json_like_str('tt','"tt":"123",')
    print parse_json_like_str('tt','\'tt\'":"123",')
    print parse_json_like_str('tt','tt:"123",')
    print parse_json_like_str('tt','"tt":123,')
    print parse_json_like_str('tt','"tt":"123",')
    print parse_json_like_str('tt','"tt":\'123\',')