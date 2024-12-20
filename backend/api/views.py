import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_home(request, *args, **kwargs):
    print(request.GET) # URL query params
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    print(data)
    # data['headers'] = request.headers # request.META ->
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers) 
    data['content_type'] = request.content_type
    return JsonResponse(data)
