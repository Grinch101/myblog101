import json
from json.encoder import JSONEncoder
from django import http
from django.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Blog
from django.core.serializers import serialize
import os
from django import db
# Create your views here.


@api_view(['POST', 'GET'])
def index(req):
    if req.method == 'GET':
        a = db.connection.settings_dict["ENGINE"]
        return JsonResponse('You can POST to this URL to save your message. Acceptable format: {title:YourTitle , body:Your Text Body} to see all records see /getall', safe=False)
    body = json.loads(req.body)
    title = body['title']
    text = body['body']
    b = Blog(title=title, body=text)
    b.save()
    return JsonResponse("SAVED", safe=False)


@api_view(['GET'])
def get_all(req):
    res = Blog.objects.all()
    res = serialize('json',res)
    res = json.loads(res)
    res = [ x['fields'] for x in res ]
    db_name = db.connection.settings_dict["ENGINE"]
    return JsonResponse({"db.connection.settings_dict['ENGINE']": db_name, "data": res}, safe=False)