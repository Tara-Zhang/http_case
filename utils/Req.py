import json
import requests


class Req(object):

    def send_post(self, url, data, header=None):
        if header == None:
            res = requests.post(url, data).json()
        else:
            res = requests.post(url, data,headers=header).json()
        return json.dumps(res,indent=2)

    def send_get(self, url, data, header):
        if header == None:
            res = requests.get(url, data).json()
        else:
            res = requests.get(url, data,headers=header).json()
        return json.dumps(res,indent=2)

    def send_main(self, url, data, method,header=None):
        if method == "POST":
            res = self.send_post(url, data, header)
        elif method == "GET":
            res = self.send_get(url, data, header)
        return res

if __name__ == '__main__':
    url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
    data = {
        'cart': '11'
    }
    a = Req()
    req = a.send_main(url, data, "GET")
    print(req)
