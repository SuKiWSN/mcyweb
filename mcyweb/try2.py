import pandas as pd
import requests

downloadHost = "https://blog.luckly-mjw.cn/tool-show/m3u8-downloader/index.html?source=https://d2dchjwa8oh2hv.cloudfront.net/api/m3u8/decode/authPath?path=jpb/20240527/ik/sw/5k/s8/5fc17ab144de4dd89d108793f09af1ad.m3u8&auth_key=1730024937-129532217-8-5a6f2a555ea56c732a956bbabeacff71"


if __name__ == '__main__':
    # df = pd.read_csv('../static/video.csv', header=0, index_col=0, sep=',')
    # videoUrl = df.loc[:, 'videoUrl']
    # print(videoUrl)
    # videoUrl.to_csv('./videoUrl.txt', index=False)
    res = requests.get(downloadHost)
    res.encoding = 'utf-8'
    print(res.text)