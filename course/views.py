from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.viewsets import ViewSetMixin
from course import models
from rest_framework.views import APIView
from rest_framework import serializers, generics
from course import models
from arrange import models
from rest_framework import exceptions
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseBaseInfo
        fields = "__all__"


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassroomInfo
        fields = "__all__"


class ClassroomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ClassroomInfo.objects.all()
    serializer_class = ClassroomSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CourseBaseInfo.objects.all()
    serializer_class = CourseSerializer


class CourseView(APIView):

    def get(self, request, *args, **kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')  # 课程id
            # 课程详细对象
            obj = models.CourseBaseInfo.objects.filter(pk=pk).first()

            ser = CourseSerializer(instance=obj, many=False)
            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 1001
            ret['error'] = "获取课程失败"

        return Response(ret)
