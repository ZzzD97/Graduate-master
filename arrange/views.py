from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.viewsets import ViewSetMixin
from course import models
from arrange import models
from rest_framework.views import APIView
from rest_framework import serializers


# Create your views here.
class CourseTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'

    name = serializers.CharField(min_length=2, error_messages={'required': '该字段必填'})
    authors = serializers.CharField(required=False)


class Coursetable(APIView):
    def get(self, request, *args, **kwargs):
        ret = models.CourseTable.objects.all()
        # 生成一个序列化的对象,传参数
        # 序列化多条,记住many=True
        coursetable_ser = CourseTableSerializer(ret, many=True, context={'request': request})
        print(coursetable_ser.data)
        return Response(coursetable_ser.data, safe=False)

    def post(self, request, *args, **kwargs):
        # 前端传递过来的数据从data中取
        # 用序列化类的数据校验
        # data参数,是要校验的数据
        response = {'status': 1000, 'msg': '成功'}
        ser = CourseTableSerializer(data=request.data)
        if ser.is_valid():
            # 如果数据校验通过,is_valid是True
            # 保存到数据库,ser是谁的对象?继承了ModelSerializer的类的对象
            ser.save()
        else:
            response['status'] = 1001
            response['msg'] = ser.errors
        return Response(response, safe=False)
