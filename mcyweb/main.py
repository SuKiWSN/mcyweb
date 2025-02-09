from . import getlist
from . import decodeData
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
import time
from model.models import favorite, videos
from django.shortcuts import render, redirect
import hashlib
import requests
import mcyweb.cfg
from mcyweb.getlist import get_headers, decode
cfg = mcyweb.cfg.CFG()

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
        'Authorization': cfg.get_token(),
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
        'User-Mark': 'xhp',
        's': s,
        't': t,
        'Referer': 'https://d2dchjwa8oh2hv.cloudfront.net/play/28620',
        'Accept': 'application/json, text/plain, */*',
        'Pragma': 'no-cache',
    }
    dlist = []
    try:
        videoId = int(data)
        video = getlist.get_data(videoId)
        video = json.loads(video)
        dlist.append([video["videoId"], cfg.img_server+video["coverImg"][0], video["title"], video["height"], video["width"], video["price"]])
    except:
        pass
    for searchType in range(1, 3):
        url = cfg.host + f"/api/search/keyWord?page={page}&pageSize=20&searchType={searchType}&searchWord={data}"
        res = requests.get(url, headers=headers)
        js = json.loads(res.text)
        video_list = []
        if "encData" in js.keys():
            encdata = js['encData']
            decodedcode = getlist.decode(encdata)
            decodedcode = json.loads(decodedcode)
            videolist = decodedcode['videoList']
            for video in videolist:
                video_list.append([video['videoId'], cfg.img_server +video['coverImg'][0], video['title'], video['height'], video['width'], video['price']])
            dlist.extend(video_list)
    return dlist


def getStation(request):
    url = cfg.host + "/api/video/getStations?classifyId=dddd".replace("dddd", request.POST.get("stationId"))
    headers = get_headers()
    res = requests.get(url, headers=headers)
    decodedData = json.loads(decode(json.loads(res.text)["encData"]))
    return JsonResponse(decodedData)


def returnlist(request):
    station_list = [144, 203, 202]
    type1 = request.POST.get('type1')
    type2 = request.POST.get('type2')
    page = request.POST.get('page')
    page = int(page)
    if type2 == "39":
        videos = getdatafromdatabase()
        videos = videos[(page-1)*50: page*50]
    elif type2 == "0":
        text = request.POST.get('text')
        videos = search(page, text)
    elif int(type2) in station_list:
        videos = getlist.getStationMore(type2, page)
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
    id = int(videoId)
    video = videos.objects.filter(videoId=id)
    # if len(video) != 0:
    #     param = video[0].videoUrl
    # else:
    if cfg.authExp is None or time.time() > cfg.authExp:
        data = getlist.get_data(319037)
        data = json.loads(data)
        authKey = data["authKey"]
        cfg.authExp = time.time() + 600
        cfg.authKey = authKey
    data = getlist.get_data(videoId)
    data = json.loads(data)
    videoUrl = data['videoUrl']
    authKey = cfg.authKey
    param = "path=" + videoUrl + "&auth_key=" + authKey
    videos(videoId=int(videoId), videoUrl=param).save()
    return JsonResponse({"data": param})

def getStationMore(request):
    station_id = request.POST.get("stationId")
    page = request.POST.get("page")
    data = getlist.getStationMore(station_id, page)
    return JsonResponse({"data": data})


def submitlike(request):
    videoid = request.POST.get('videoUrl')
    imgurl = request.POST.get('imgurl')
    title = request.POST.get('title')
    price = request.POST.get('price')
    if len(favorite.objects.filter(videoId=videoid)) == 0:
        favorite(address="27796554", videoId=int(videoid), videoTitle=title, ImageUrl=imgurl, price=int(price)).save()
        print(videoid, imgurl, title, price, "保存成功")
    else:
        print(videoid, imgurl, title, price, "已收藏")
    return JsonResponse({"data": "success"})