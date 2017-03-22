from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import json

def index(request):


    return render(request,"index.html")

def ajax1(request):
    print(request.GET)
    return HttpResponse("Ok")

def ajax2(request):
    if request.method=="GET":
        username = request.POST.get("username")
        data = {'k': username, "k1": "你好啊"}
        msg = json.dumps(data, ensure_ascii=False)
        return HttpResponse(msg)
    if request.method == "POST":
        username =request.POST.get("root")
        data = {"status":True,'k': username,"k1":"你好啊"}
        print(request.GET)
        print(request.POST)
        # print(request.FILES)
        data =json.dumps(data,ensure_ascii=False)
        return HttpResponse(data)

def ajax3(request):
    if request.method=="GET":
        username = request.POST.get("username")
        data = {'k': username, "k1": "你好啊"}
        msg = json.dumps(data, ensure_ascii=False)
        return HttpResponse(msg)
    if request.method == "POST":
        username =request.POST.get("k1")
        data = {"status":True,'k': username,"k2":"你好啊"}
        k1 = request.POST.get("k1")
        k2 = request.POST.get("k2")
        files= request.FILES.get("k3")
        # print(dir(files))
        f = open(files.name,"wb")
        for i in files:
        # for i in files.chunks: ?????????????????????
            f.write(i)
        f.close()

        print(request.POST,k1,k2)
        print(request.FILES)

        data =json.dumps(data,ensure_ascii=False)
        return HttpResponse(data)
        # return HttpResponse("ok")