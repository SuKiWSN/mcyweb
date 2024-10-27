from decodeData import AESCipher
import time
import hashlib
import requests
import json
from mcyweb.cfg import CFG
cfg = CFG()

def request(page):
    url = f"https://mhw.vxdtmee.xyz/api/community/dynamic/list?loadType=1&page={page}&pageSize=30"
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()
    headers = {
        'Authorization': cfg.token,
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8',
        'User-Mark': 'xhp',
        's': s,
        't': t,
    }
    res = requests.get(url, headers=headers)
    return res.text


def get_list(encdata):
    img_root = "https://imadcg.dadi1688.cn/"
    encdata = json.loads(encdata)
    encdata = encdata['encData']
    data = decode(encdata)
    data = json.loads(data)
    data = data['data']
    print(data)
    for item in data:
        title = item['content']
        title = title.replace('/', '').replace('-', '').split('\n')[0]
        idx = 1
        video = item['video']
        if video is not None:
            videoUrl = video['videoUrl']
            authKey = video['authKey']
            videoUrl = "https://mhw.vxdtmee.xyz/api/m3u8/decode/authPath?" + "path=" + videoUrl + "&auth_key=" + authKey
            with open('video.txt', 'a') as f:
                f.write(videoUrl + '\n')
        imgs = item['dynamicImg']
        if imgs is not None:
            for img in imgs:
                imgUrl = img_root + img
                imgContent = requests.get(imgUrl)
                imgContent = decodeImg(imgContent.content)
                with open(f'../output/{title}_{idx}.jpg', 'wb') as f:
                    f.write(imgContent)
                    idx += 1


def decodeImg(imgContent):
    r = "2020-zq3-888"
    byte = bytearray(imgContent)
    for i in range(100):
        byte[i] ^= ord(r[i % len(r)])
    byte[100:] = imgContent[100:]
    return byte



def decode(encdata):
    token = 'JhbGciOiJIUzI1Ni'
    a = AESCipher(secretkey=token)
    decodedcode = a.decrypt(encdata)
    return decodedcode

if __name__ == '__main__':
    for page in range(1, 100):
        print(page)
        encdata = request(page=page)
        get_list(encdata)