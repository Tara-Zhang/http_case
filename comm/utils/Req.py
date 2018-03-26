import json
import requests


class Req(object):
    def __init__(self):
        self.session = requests.session()
    def get_response(self, method, url, variable=None, para=None, json=None, data=None, header=None, files=None, cookie=None):

        res = self.session.request(method, url, params=para, json=json, data=data, headers=header, files=files,
                               cookies=cookie)

        return res.text

if __name__ == '__main__':
    url = 'http://www.imooc.com//or/shop?groupID=11157&businessType=1&pageNum=1&lng=116.34619903564453&lat=39.939613342285156&groupID=11157'
    data = {
        'cart': '11'
    }

    a = Req()
    req = a.get_response(url = url, method='get', data =data)
    print(req)
