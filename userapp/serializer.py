from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from userapp.models import User, Employee


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    extra_kwargs = {
        "username": {
            "required": True,
            "min_length": 2,
        },
    }
    def validate(self, attrs):
        return attrs

    def validate_username(self, value):
        emp = User.objects.filter(username=value)
        print('emp1=',emp)
        if emp:
            raise serializers.ValidationError('该账户已存在')
        return value
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "emp_name", "salary", "full_img", "age", "img")
        extra_kwargs = {
            "full_img": {
                "read_only": True,
            },
            "img": {
                "write_only": True
            },
            "emp_name":{
                "min_length":2,
                "required": True,
            }
        }

    def validate(self, attrs):
        return attrs

    def validate_emp_name(self, value):
        emp = Employee.objects.filter(emp_name=value)
        print('emp=',emp)
        if emp:
            raise serializers.ValidationError('该员工已存在')
        return value

