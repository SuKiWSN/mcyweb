import requests
from decodeData import AESCipher
import time
import hashlib
import json

def get_s_t():
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()
    return s, t

def send_request(url):
    s, t = get_s_t()
    headers = {
        'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMjM5Mjk3MyIsImlzcyI6IiIsImlhdCI6MTY5MDE5OTQ2MSwibmJmIjoxNjkwMTk5NDYxLCJleHAiOjE4NDc4Nzk0NjF9.nywATjJmSZ27dDz_jdTyRQKyDKYuFyHAoivMs5zKq_I',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
        'User-Mark': 'xhp',
        's': s,
        't': t,
        'Referer': 'https://mhw.vxdtmee.xyz/play/28620',
        'Accept': 'application/json, text/plain, */*',
        'Pragma': 'no-cache',
    }
    res = requests.get(url, headers=headers)
    return res.text
if __name__ == '__main__':
    decoder = AESCipher()
    url = "https://mhw.vxdtmee.xyz/api/video/classify/getClassifyVideos?classifyId=14&page=3&pageSize=20&sortNum=1&_t=1693584149483"
    text_data = send_request(url)
    js_data = json.loads(text_data)
    if js_data['code'] == 200:
        encdata = js_data['encData']
        data = decoder.decrypt(encdata)
        print(data)