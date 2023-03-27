from . import getlist
from . import decodeData
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
import time
from model.models import favorite
from django.shortcuts import render, redirect
import hashlib
import requests

def home(request):
    return render(request, 'home.html')

def search(page, data):
    ts = time.time()
    t = str(ts).split('.')[0] + str(ts).split('.')[1][:3]
    ts = t[3: 8]
    hl = hashlib.md5()
    hl.update(ts.encode(encoding='utf8'))
    s = hl.hexdigest()
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
    dlist = []
    for searchType in range(1, 3):
        url = f"https://mhw.vxdtmee.xyz/api/search/keyWord?page={page}&pageSize=20&searchType={searchType}&searchWord={data}"
        res = requests.get(url, headers=headers)
        js = json.loads(res.text)
        video_list = []
        encdata = js['encData']
        decodedcode = getlist.decode(encdata)
        decodedcode = json.loads(decodedcode)
        videolist = decodedcode['videoList']
        for video in videolist:
            video_list.append([video['videoId'], 'https://ivnwevs.chen6666.top/'+video['coverImg'][0], video['title'], video['height'], video['width'], video['price']])
        dlist.extend(video_list)
    return dlist
def returnlist(request):
    type1 = request.POST.get('type1')
    type2 = request.POST.get('type2')
    page = request.POST.get('page')
    page = int(page)
    if type2 == "1":
        videos = getdatafromdatabase()
        videos = videos[(page-1)*50: page*50]
    elif type2 == "0":
        text = request.POST.get('text')
        videos = search(page, text)
    else:
        videos = getlist.get_list(type2, page)
    return JsonResponse({"data": videos})

def getdatafromdatabase():
    datas = favorite.objects.filter()
    videos = []
    for data in datas:
        videos.append([data.videoId, data.ImageUrl, data.videoTitle, 0, 0, data.price])
    return videos

def getvideo(request):
    videoId = request.POST.get('videoId')
    data = getlist.get_data(videoId)
    data = json.loads(data)
    videoUrl = data['videoUrl']
    return JsonResponse({"data": videoUrl})

def submitlike(request):
    videoid = request.POST.get('videoUrl')
    imgurl = request.POST.get('imgurl')
    title = request.POST.get('title')
    price = request.POST.get('price')
    print(videoid, imgurl, title, price)
    favorite(address="27796554", videoId=int(videoid), videoTitle=title, ImageUrl=imgurl, price=int(price)).save()
    return JsonResponse({"data": "success"})