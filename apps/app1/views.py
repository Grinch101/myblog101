import json
from json.encoder import JSONEncoder
from django import http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Blog
from django.core.serializers import serialize

# Create your views here.


@api_view(['POST', 'GET'])
def index(req):
    return JsonResponse(json.loads(req.body))


@api_view(['GET'])
def get_all(req):
    res = Blog.objects.all()
    res = serialize('json', res)
    print(res)
    return JsonResponse({"YES":"IT IS RESPONSE"}, safe=False)