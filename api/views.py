from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api.authentiactions import MyAuth
from api.models import User
from api.permission import MyPermission
from api.throttles import MySendMessageRate


class Demo(APIView):
    def get(self,request,*args,**kwargs):
        user=User.objects.first()
        print('user',user)
        print('user_group',user.groups.first())
        print('user_group_permission',user.user_permissions.first())

        return Response("ok")
class UserAPI(APIView):
    authentication_classes = [MyAuth]
    permission_classes = [MyPermission]
    throttle_classes = [MySendMessageRate]

    def get(self, request, *args, **kwargs):
        print("读请求")
        return Response("读请求")

    def post(self, request, *args, **kwargs):
        print("写请求")
        return Response("写请求")
