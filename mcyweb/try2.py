import requests
import time
import hashlib
import json
def travel():
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()
    # url = "https://yuseman.cusfjengbk.work/api/user/traveler"
    url = "https://d2dchjwa8oh2hv.cloudfront.net/api/user/traveler"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8',
        'User-Mark': 'xhp',
        'Content-Type': "application/json;charset=UTF-8",
        's': s,
        't': t,
        'Connection': "keep-alive",
    }
    data = {
        "deviceId":"6b13f3fd-a974-4a2d-bf78-8165fd24e614","code":"{}","chCode":""}
    res = requests.post(url, headers=headers, data=json.dumps(data))
    return res.text

def get_data(id):
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()
    url = "https://yuseman.cusfjengbk.work/api/video/getVideoById?videoId={}".format(id)
    headers = {
        'Authorization': "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0NjEwMTgiLCJpc3MiOiIiLCJpYXQiOjE3Mzg3MzY2NzIsIm5iZiI6MTczODczNjY3MiwiZXhwIjoxODk2NDE2NjcyfQ.GZHMj_ia1Unrmv_p-5sAhSGBLj-0THHdCX-jCdvaFKw",
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.10.8',
        'User-Mark': 'xhp',
        's': s,
        't': t,
        'Connection': "keep-alive",
    }
    "https://yuseman.cusfjengbk.work/api/m3u8/decode/authPath?path=jpc/20241113/cl/kw/q0/vg/98203ac34c724f07ba0a5412042ad2f7.m3u8&auth_key=1738743697-1461018-30-aa8968032b5ed0f3da037f68f6501d35&id=6788d5f9f646721ce98f1731"
    res = requests.get(url, headers=headers)
    js = json.loads(res.text)
    return js


if __name__ == '__main__':

    js = get_data(83410)
    data = js["data"]
    title = data["title"]
    price = data["price"]
    print(data["authKey"])
    videoUrl = "https://yuseman.cusfjengbk.work/api/m3u8/decode/authPath?path="+data["videoUrl"] + "&auth_key=1738747748-1461018-30-593068a6a6ed98ae13cc81a508474dd1&id=6788d5f9f646721ce98f1731"
    canWatch = data["canWatch"]

    print(canWatch, title, price, videoUrl)
    "https://yuseman.cusfjengbk.work/api/m3u8/decode/authPath?path=lfb/c8/ce/6b/qh/07b666d3638f43acb8309ecf31c982aa.m3u8&auth_key=1738747748-1461018-30-593068a6a6ed98ae13cc81a508474dd1&id=6788d5f9f646721ce98f1731"
    "https://yuseman.cusfjengbk.work/api/m3u8/decode/authPath?path=jpc/20241127/lt/jj/xr/26/3e3ae162e4444555ae35d2eae63e1b27.m3u8&auth_key=1738738347-1461018-30-54b856d6a391b783fb1b6af79ce07372&id=6788d5f9f646721ce98f1731"
    "https://yuseman.cusfjengbk.work/api/m3u8/decode/authPath?path=lfb/wy/00/fw/j6/107d44888c924146b816722169599625.m3u8&auth_key=1738744219-1461018-30-7d89276c3f33deffc84ae1bf9fed0cca&id=6788d5f9f646721ce98f1731"
    "&auth_key=1738745050-130549107-8-a52530adba7956bd8fc4678dfa25caf7"
    "https://d2dchjwa8oh2hv.cloudfront.net/api/m3u8/decode/authPath?path=jpb/20241128/di/dl/l5/nv/f7562591728145d9a33b109ca00326ec.m3u8&auth_key=1738745050-130549107-8-a52530adba7956bd8fc4678dfa25caf7"
    "lfb/c8/ce/6b/qh/07b666d3638f43acb8309ecf31c982aa.m3u8"