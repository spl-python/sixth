from rest_framework import mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.models import Employee, User
from userapp.serializer import EmployeeSerializer, UserSerializer
from utils.response import APIResponse


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        user_obj = User.objects.filter(username=username, password=password).first()
        print(username,password)
        if user_obj:
            data = UserSerializer(user_obj).data
            return Response({"results": data, "message": True}, status=status.HTTP_200_OK)
        return Response({"results": "登录参数有误", "message": False}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()

        return Response({"results": UserSerializer(user_obj).data})

class EmployeeAPIView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self,request,*args,**kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=response.data)