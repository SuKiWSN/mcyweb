import requests
import time
import hashlib
import json
from mcyweb.decodeData import AESCipher

def get_list(kind_id, page):
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()


    url = 'https://mhw.vxdtmee.xyz/api/video/classify/getClassifyVideos?classifyId=1&page=1&pageSize=50&sortNum=1'
    url = url.replace('page=1', 'page={}'.format(page)).replace('classifyId=1', 'classifyId={}'.format(kind_id))
    headers = {
            'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxODU0MjUzNiIsImlzcyI6IiIsImlhdCI6MTY3OTIwNTcyOCwibmJmIjoxNjc5MjA1NzI4LCJleHAiOjE4MzY4ODU3Mjh9.HvG0U-1ZhkhBD9QMQ3Jo9XCeNToQvLYYo5_Auo7Whhw',
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
        imageUrl = 'https://ivnwevs.chen6666.top/' + i['coverImg'][0]
        print(i['coverImg'][0])
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
    url = 'https://mhw.vxdtmee.xyz/api/video/getVideoById?videoId={}'.format(id)
    headers = {
        'Authorization': "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxODU0MjUzNiIsImlzcyI6IiIsImlhdCI6MTY3OTIwNTcyOCwibmJmIjoxNjc5MjA1NzI4LCJleHAiOjE4MzY4ODU3Mjh9.HvG0U-1ZhkhBD9QMQ3Jo9XCeNToQvLYYo5_Auo7Whhw",
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8',
        'User-Mark': 'xhp',
        's': s,
        't': t,
    }
    res = requests.get(url, headers=headers)
    js = json.loads(res.text)
    encdata = js['encData']
    decodedcode = decode(encdata)
    return decodedcode