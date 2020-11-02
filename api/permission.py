from rest_framework.permissions import BasePermission

from api.models import User


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in("GET","HEAD","OPTIONS"):
            return True
        username=request.data.get("username")
        user=User.objects.filter(username=username).first()
        print("user",user)
        if user:
            print('权限够了')
            return True
        print('权限不足')
        return False