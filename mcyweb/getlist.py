import requests
import time
import hashlib
import json
from mcyweb.decodeData import AESCipher
from mcyweb.cfg import CFG
cfg = CFG()

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
            'Authorization': cfg.token,
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
    encdata = js['encData']
    decodedcode = decode(encdata)
    # print(decodedcode)
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
    url = url.replace('page=1', 'page={}'.format(page))
    headers = {
        'Authorization': cfg.token,
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
    encdata = js['encData']
    decodedcode = decode(encdata)
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
        'Authorization': cfg.token,
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8',
        'User-Mark': 'xhp',
        's': s,
        't': t,
        'Connection': "close",
    }
    res = requests.get(url, headers=headers)
    res.close()
    js = json.loads(res.text)
    encdata = js['encData']
    decodedcode = decode(encdata)
    return decodedcode

if __name__ == '__main__':
    "https://mhw.vxdtmee.xyz/api/m3u8/decode/authPath?path=mib/db/om/cs/my/46bfe0f82cdc4a33b10e6ed2a6916583.m3u8&auth_key=1704095250-023460332-8-85a39f52dc08568f584a2d6ae34578d5"
    data = "1704095250"
    data = encode(data)
    "https://d2dchjwa8oh2hv.cloudfront.net/play/311897"
    "https://d2dchjwa8oh2hv.cloudfront.net/api/m3u8/decode/authPath?path=jpd/20240921/8g/x7/2p/5f/a4eb8c1ed39140fb9e1b643897f49be6.m3u8&auth_key=1730011562-029532217-8-aae353d75553661d388327633359898e"
    # https://d2dchjwa8oh2hv.cloudfront.net/api/m3u8/decode/authPath?path=spg/20240126/id/4d/u6/tn/d90e486c73044146872bbccca9d2de3f.m3u8&auth_key=1729219585-129532217-8-2fcb0ee16cd2b9e050976b30b037919d
# spg/20240126/id/4d/u6/tn/d90e486c73044146872bbccca9d2de3f.m3u8&auth_key=1729219821-029528907-8-65d68b593ec0ba9b6a71cbb2a67fbdf2
    print(len("85a39f52dc08568f584a2d6ae34578d5"))
    print(data)
