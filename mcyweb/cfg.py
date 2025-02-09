import json
import hashlib
import requests
import time

class CFG():
    def __init__(self):
        self.img_server = "https://dg2ordyr4k5v3.cloudfront.net/"
        self.host = "https://d2dchjwa8oh2hv.cloudfront.net"
        # self.host = "https://yuseman.cusfjengbk.work"
        # self.img_server = "https://ssim.ctlweb.site/"
        self.authKey = None
        self.authExp = None

    def travel(self):
        ts = time.time()
        t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
        ts = t[3: 8]
        hl = hashlib.md5()
        hl.update(ts.encode(encoding='utf8'))
        s = hl.hexdigest()
        # url = "https://yuseman.cusfjengbk.work/api/user/traveler"
        url = self.host + "/api/user/traveler"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8',
            'User-Mark': 'xhp',
            'Content-Type': "application/json;charset=UTF-8",
            's': s,
            't': t,
            'Connection': "keep-alive",
        }
        data = {
            "deviceId": "6b13f3fd-a974-4a2d-bf78-8165fd24e614", "code": "{}", "chCode": ""}
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res.text

    def get_token(self):
        return json.loads(self.travel())["data"]["token"]


if __name__ == '__main__':
    cfg = CFG()
    print(cfg.token)