import json
import requests


class Req(object):

    def get_response(self, url, data, method,header=None):

        res = requests.request(url,data)

        return res

if __name__ == '__main__':
    url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
    data = {
        'cart': '11'
    }
    a = Req()
    req = a.get_response(url, data, "get")
    print(req)
