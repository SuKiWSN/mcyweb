from decodeData import AESCipher
import time
import hashlib
import requests
from io import BytesIO
import os
import json
from download_video import download_video
from PIL import Image
from tqdm import tqdm
from getlist import get_headers
import PIL
from multiprocessing import Pool
from mcyweb.cfg import CFG
cfg = CFG()
session = requests.session()

def request(page):
    url = cfg.host + f"/api/community/dynamic/list?loadType=1&page={page}&pageSize=30"
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
    res = requests.get(url, headers=headers)
    return res.text


def get_list(encdata):
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
            videoUrl = cfg.host+"/api/m3u8/decode/authPath?" + "path=" + videoUrl + "&auth_key=" + authKey
            # download_video(videoUrl, title)
            with open('video.txt', 'a') as f:
                f.write(videoUrl + '\n')
        imgs = item['dynamicImg']
        if imgs is not None:
            with Pool(16) as pool:
                images = pool.map(download, imgs)
            for imgContent in images:
                imgContent.save(f'../output/{title}_{idx}.jpg')
                idx += 1
                # with open(f'../output/{title}_{idx}.jpg', 'wb') as f:
                #     f.write(imgContent)
                #     idx += 1


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

def download(url):
    print(url)
    res = session.get(cfg.img_server+url)
    while res.status_code != 200:
        res = session.get(cfg.img_server + url)
        print("retry")
    img = decodeImg(res.content)
    img = BytesIO(img)
    img = Image.open(img).convert("RGB")
    return img


if __name__ == '__main__':
    # imgUrl = "image/jz/r8/sg/90/1dc425f0fa2a4b0aad2421bcaf958604.jpeg"
    # img = download(imgUrl)
    # img.save("output.jpg")
    # exit()
    # for page in range(1, 100):
    #     print(page)
    #     encdata = request(page=page)
    #     get_list(encdata)
    # url = cfg.img_server+"comics/4o/rl/b1/n0/94d4eb71-eaa4-4da6-a6c6-af15f6c9d909-1713.jpg"
    # res = requests.get(url)
    # img = res.content
    # img = decodeImg(img)
    # print(url)
    # with open("output.jpg", "wb") as f:
    #     f.write(img)
    # exit()
    info_url = cfg.host + "/api/comics/base/info?comicsId=5985&_t=1738853572595"
    url = cfg.host + "/api/comics/base/chapterInfo?chapterId=228223&_t=1738848300863"
    headers = get_headers()
    res = requests.get(info_url, headers=headers)
    res = json.loads(res.text)
    if "encData" in res.keys():
        data = res["encData"]
        data = decode(data)
        data = json.loads(data)
    else:
        data = res["data"]
    title = data["comicsTitle"]
    os.makedirs(title, exist_ok=True)
    chapterList = data["chapterList"]
    for chapter in chapterList[0:]:
        chapterId = chapter["chapterId"]
        chapterTitle = chapter["chapterTitle"]
        chapterUrl = url.replace("228223", str(chapterId))
        headers = get_headers()
        res = session.get(chapterUrl, headers=headers)
        res = json.loads(res.text)
        if "encData" in res.keys():
            data = decode(res["encData"])
            data = json.loads(data)
        else:
            data = res["data"]
        print(chapterTitle, chapter)
        print(data)
        with Pool(6) as pool:
            images = pool.map(download, data["imgList"])
        images[0].save("{}/{}.pdf".format(title, chapterTitle), save_all=True, append_images=images[1:], resolution=150.0, quality=95)

    exit()
    url = "https://d2dchjwa8oh2hv.cloudfront.net/api/comics/base/chapterInfo?chapterId=228223&_t=1738848300863"
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
    res = requests.get(url, headers=headers)
    res = json.loads(res.text)
    data = decode(res["encData"])
    data = json.loads(data)
    print(data)
    exit()
    with Pool(16) as pool:
        images = pool.map(download, data["imgList"])
    images[0].save("output.pdf", save_all=True, append_images=images[1:], resolution=100.0, quality=95)