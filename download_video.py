import os.path

import requests
import subprocess
import m3u8


# m3u8 链接
def download_video(url, title):
    # 下载 m3u8 文件内容
    response = requests.get(url)
    m3u8_content = response.text

    # 解析 m3u8 内容，找到加密信息和密钥路径
    playlist = m3u8.loads(m3u8_content)
    print(url)
    key_uri = playlist.keys[0].uri if playlist.keys else None  # 获取密钥链接
    if not key_uri:
        return

    # 下载加密密钥
    key_url = key_uri if key_uri.startswith('http') else url.rsplit('/', 1)[0] + '/' + key_uri
    key_response = requests.get(key_url)
    with open('video.key', 'wb') as f:
        f.write(key_response.content)

    # 使用 ffmpeg 下载并解密视频流
    # 这里 -decryption_key 是我们刚下载的密钥
    cnt = 1
    while os.path.exists("./output/{}-{}.mp4".format(title, cnt)):
        cnt += 1
    subprocess.run(['ffmpeg', '-i', url, '-c', 'copy', '-decryption_key', 'video.key', '../output/{}-{}.mp4'.format(title, cnt)])


if __name__ == '__main__':
    download_video(url="https://d2dchjwa8oh2hv.cloudfront.net/api/m3u8/decode/authPath?path=jpd/20250118/9y/2j/bc/9b/911714b2711d4f4fbf4130a0079921ff.m3u8&auth_key=1738852856-130549107-8-b85df074d9ffd4c2be2e85a4dcf66613", title="1")