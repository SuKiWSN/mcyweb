import requests
import time
import hashlib
import json
from mcyweb.decodeData import AESCipher
from mcyweb.cfg import CFG
cfg = CFG()

def decode(encdata):
    token = 'JhbGciOiJIUzI1Ni'
    a = AESCipher(secretkey=token)
    decodedcode = a.decrypt(encdata)
    return decodedcode
def get_list(kind_id, page):
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()

    url = "https://mhw.vxdtmee.xyz/api/comics/base/chapterInfo?chapterId=91484&_t=1702120774809"
    # url = 'https://mhw.vxdtmee.xyz/api/comics/base/findList?categoryId=209&orderType=1&page=8&pageSize=30&_t=1702119520536'
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
    print(res.text)
    js = json.loads(res.text)
    id_list = []
    encdata = js['encData']
    decodedcode = decode(encdata)
    data = json.loads(decodedcode)
    print(data)
    data = data['data']
    for i in data:
        videoid = i['videoId']
        imageUrl = 'https://ivnwevs.chen6666.top/' + i['coverImg'][0]
        height = i['height']
        width = i['width']
        title = i['title']
        price = i['price']
        # print(i)
        id_list.append([videoid, imageUrl, title, height, width, price])
    return id_list

if __name__ == '__main__':
    get_list(0, 1)