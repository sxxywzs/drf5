from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from api.models import User


class MyAuth( BaseAuthentication ):

    def authenticate(self, request):
        auth = request.META.get( 'HTTP_AUTHORIZATION', None )
        print( 'auth,auth,auth', auth )

        if auth == None:
            return None

        user=User.objects.filter(username=auth).first()

        if not user:
            raise exceptions.AuthenticationFailed("用户不存在")

        return user,None