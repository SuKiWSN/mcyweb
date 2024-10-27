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
    }
    res = requests.get(url, headers=headers)
    js = json.loads(res.text)
    encdata = js['encData']
    decodedcode = decode(encdata)
    print(decodedcode)
    return decodedcode

if __name__ == '__main__':
    "https://mhw.vxdtmee.xyz/api/m3u8/decode/authPath?path=mib/db/om/cs/my/46bfe0f82cdc4a33b10e6ed2a6916583.m3u8&auth_key=1704095250-023460332-8-85a39f52dc08568f584a2d6ae34578d5"
    data = "GulIpz5dLhLk/1muLo660Vfoyrt64JqOjSx89ocLbTnLoolJMdrJXaZ0mgO4BSnxwCVy7t7H41qOobOxPuLuSrGUHBF5XopG8pQFihWSOqvSxP/6Sua3x08EP82tlTkaVYMOVGy11/ofAYqhV1qLdvI9Swy/ZRbTNN9PEcw5lRV0lg8WBzgUZP0FHQpmg9puZxDspbYCFdQOuse2mmDcy0WOSGBQ4jAmlZnlzrlJrmHS+7eGoE5fKgTa3HcBYLVe9dRNNLfgxp+F0pGMYiUvlansDarTr9hp+wFxkhIwh5HhB54zu5Jt05+9fqD4vaTGDSbUE4Jncm701iLE5fx7fvocvUBI7XP6DnoltI6nyvf6aehhVlkqGp7kp+PhEWVomQQdasNJN0ivnrTGLoH/luXAoZTuxLS+Kqiev/P1KRCbRKdx3oyLwJclUMM5xrK8WFwki5/iRDP3+OwtiOwf7wzwu4sw80eLo0bxkOU0uxtqDxnm2YIpI9fMIoJWDagSsS4PgHvJYMVZRKFyAEdm1PnQOdgbihU8PxeRUWzKhPefF1RAEQZ5a2WfOfceSLXGt2vdB9XTeQzchOujE6irZeVVwppsMw1I+eXpUkxeNFe27hr7Zet6d7G3JXt2mkwWpJlv+p752jQYCz2y+oTLdyDIis/N2oqVbL/1kferhqwwMVvIWXxg708ZJjxrRuwBGTSIfngrBfpSvL+JrAtwCw/EdQxj/bBYRHisV0rnFLzJth0l2cIHuEwUGFeoTvL8mTS3Ty7YwN4Xh3VqS98Rp87dPYKxrpVKEHC/1bA/Gqdn29dhTUI/vcimgMfoFq20DlEg4v1TKm26drE3OFHB6DIkIVtZJgmK8eWgEojmJXWrz0zaIcO6fxFUfmEu+FuPd/QDt2Vtio+e7SON2OxhZ6WgCucGkkxexPua64UFn3xgeWwFs86vYGCUWHStCaplEmvxoAKkTwW2flCAAKNy/Y7fsdkHknNmMPHMWebo7Az7aW+JjWWMmBZnoGy4xqTc1gcYdVThhTHPDA1JPbwgQhnl3csBllCpoZTNpKzvgW2Wu0Zo8KQrmi9EHtycY8QOdc/aVncgPod1L4LzioZcKvkz/bayvVE0G5pVV0q9NN2rbu6gbNo+SqPxrBXd62ZKoqq9jj6aqa1U4xw82y0O8P1PqIiyue7b0Bz/RapgXW8="
    data = decode(data)
    # https://d2dchjwa8oh2hv.cloudfront.net/api/m3u8/decode/authPath?path=spg/20240126/id/4d/u6/tn/d90e486c73044146872bbccca9d2de3f.m3u8&auth_key=1729219585-129532217-8-2fcb0ee16cd2b9e050976b30b037919d
# spg/20240126/id/4d/u6/tn/d90e486c73044146872bbccca9d2de3f.m3u8&auth_key=1729219821-029528907-8-65d68b593ec0ba9b6a71cbb2a67fbdf2
    print(data)