# dojo/views,py
from django.http import HttpResponse
from django.shortcuts import render

def mysum(request , x , y=0, z=0):
    # request : HttpRequest
    result = sum(map(lambda x : int(x or 0), numbers.split("/")))
    return HttpResponse(result)