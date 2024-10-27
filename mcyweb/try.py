import time
import hashlib
from cfg import CFG
import requests
import pandas as pd
import getlist
import json
import random
cfg = CFG()
def search(page, data):
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()
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
    dlist = []
    for searchType in range(1, 3):
        url = cfg.host + f"/api/search/keyWord?page={page}&pageSize=20&searchType={searchType}&searchWord={data}"
        res = requests.get(url, headers=headers)
        js = json.loads(res.text)
        video_list = []
        encdata = js['encData']
        decodedcode = getlist.decode(encdata)
        decodedcode = json.loads(decodedcode)
        videolist = decodedcode['videoList']
        for video in videolist:
            video_list.append([video['videoId'], cfg.img_server +video['coverImg'][0], video['title'], video['height'], video['width'], video['price']])
        dlist.extend(video_list)
    return dlist

def getvideo(videoId):
    data = getlist.get_data(videoId)
    data = json.loads(data)
    videoUrl = data['videoUrl']
    authKey = data['authKey']
    param = cfg.host + "/api/m3u8/decode/authPath?" + "path=" + videoUrl + "&auth_key=" + authKey
    return param


if __name__ == '__main__':
    for page in range(10000):
        videoList = search(page, cfg.title)
        for videoInformation in videoList:
            try:
                df = pd.read_csv("../static/video.csv", sep=",", header=0, index_col=0)
            except pd.errors.EmptyDataError:
                df = pd.DataFrame(columns=['videoId', 'videoTitle', 'videoUrl'])
                df.set_index('videoId', inplace=True)
            videoId = videoInformation[0]
            videoTitle = videoInformation[2]
            try:
                videoUrl = df.at[videoId, 'videoUrl']
            except KeyError:
                videoUrl = getvideo(videoId)
                df.loc[videoId] = [videoTitle, videoUrl]
                time.sleep(random.randint(10, 20))
            print(videoId, videoTitle, videoUrl)
            df.to_csv("../static/video.csv", sep=",", header=True)


