from . import getlist
from . import decodeData
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
import time
from model.models import favorite
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def returnlist(request):
    type1 = request.POST.get('type1')
    type2 = request.POST.get('type2')
    page = request.POST.get('page')
    page = int(page)
    if type2 == "1":
        videos = getdatafromdatabase()
        videos = videos[(page-1)*50: page*50]
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