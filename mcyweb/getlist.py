import requests
import time
import hashlib
import json
from mcyweb.decodeData import AESCipher
from mcyweb.cfg import CFG
cfg = CFG()

def get_headers():
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()
    headers = {
        'Authorization': cfg.get_token(),
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8',
        'User-Mark': 'xhp',
        's': s,
        't': t,
    }
    return headers
def get_list(kind_id, page):
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()


    url = cfg.host + '/api/video/classify/getClassifyVideos?classifyId=1&page=1&pageSize=50&sortNum=1'
    url = url.replace('page=1', 'page={}'.format(page)).replace('classifyId=1', 'classifyId={}'.format(kind_id))
    headers = {
            'Authorization': cfg.get_token(),
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
            'User-Mark': 'xhp',
            's': s,
            't': t,
            'Referer': cfg.host + '/play/28620',
            'Accept': 'application/json, text/plain, */*',
            'Pragma': 'no-cache',
    }
    res = requests.get(url, headers=headers)
    js = json.loads(res.text)
    id_list = []
    if "encData" in js.keys():
        encdata = js['encData']
        decodedcode = decode(encdata)
    else:
        print(js)
        decodedcode = js["data"]
    data = json.loads(decodedcode)
    data = data['data']
    for i in data:
        videoid = i['videoId']
        imageUrl = cfg.img_server + i['coverImg'][0]
        height = i['height']
        width = i['width']
        title = i['title']
        price = i['price']
        # print(i)
        id_list.append([videoid, imageUrl, title, height, width, price])
    return id_list

def getStationMore(kind_id, page):
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()

    url = cfg.host + '/api/video/getStationMore?stationId=144&sortType=1&page=1&pageSize=16&_t=1702117835366'
    url = url.replace('page=1', 'page={}'.format(page)).replace("stationId=144", "stationId={}".format(kind_id))
    headers = {
        'Authorization': cfg.get_token(),
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
        'User-Mark': 'xhp',
        's': s,
        't': t,
        'Referer': 'https://mhw.vxdtmee.xyz/play/28620',
        'Accept': 'application/json, text/plain, */*',
        'Pragma': 'no-cache',
    }
    res = requests.get(url, headers=headers)
    js = json.loads(res.text)
    id_list = []
    if "encData" in js.keys():
        encdata = js['encData']
        decodedcode = decode(encdata)
        data = json.loads(decodedcode)
    else:
        data = js["data"]
    data = data['data']
    for i in data:
        videoid = i['videoId']
        imageUrl = cfg.img_server + i['coverImg'][0]
        height = i['height']
        width = i['width']
        title = i['title']
        price = i['price']
        # print(i)
        id_list.append([videoid, imageUrl, title, height, width, price])
    return id_list

def decode(encdata):
    token = 'JhbGciOiJIUzI1Ni'
    a = AESCipher(secretkey=token)
    decodedcode = a.decrypt(encdata)
    return decodedcode

def encode(encdata):
    token = 'JhbGciOiJIUzI1Ni'
    a = AESCipher(secretkey=token)
    encodedcode = a.encrypt(encdata)
    return encodedcode

def get_data(id):
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()
    url = cfg.host + '/api/video/getVideoById?videoId={}'.format(id)
    headers = {
        'Authorization': cfg.get_token(),
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8',
        'User-Mark': 'xhp',
        's': s,
        't': t,
        'Connection': "keep-alive",
    }
    res = requests.get(url, headers=headers)
    js = json.loads(res.text)
    if "encData" in js.keys():
        encdata = js['encData']
        decodedcode = decode(encdata)
    else:
        decodedcode = js["data"]
    return decodedcode

if __name__ == '__main__':
    data = "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"
    decoded_data = decode(data)
    print(decoded_data)
    data = json.loads(decoded_data)
    #
    # "https://ssim.ctlweb.site/jhimage/ba/wv/xb/82/e1f7aae6e9404677b44f60839bb016a7.jpg"
    #
    # print(get_data(83410))
