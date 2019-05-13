from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from course import models
from rest_framework.views import APIView
from rest_framework import serializers, mixins, viewsets, generics
from rest_framework import serializers
from teacher import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Teacher
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        try:
            # 得到关联表中的字段，必须用try,否则如果存在一个没有定义tid的教师时，系统将报错
            data['tid'] = instance.models.Teacher.tid
        except Exception as e:
            data['tid'] = ''
        return data


class TeacherEdit(mixins.ListModelMixin,  # 表示可以在Postman 类似的软件中只能查找所有数据
                  viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,  # 表示可以在Postman类似的软件中只能查找单一数据
                  mixins.UpdateModelMixin,  # 表示可以在Postman类似的软件中更新数据
                  mixins.DestroyModelMixin,  # 表示可以在Postman类似的软件中删除数据
                  mixins.CreateModelMixin):  # 表示可以在Postman类似的软件中创建数据

    # 查询所有信息
    queryset = models.Teacher.objects.all()
    # 序列化
    serializer_class = TeacherSerializer


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CollegeInfo
        fields = "__all__"


class TeacherView(APIView):
    def get(self, request, *args, **kwargs):
        """
        教师详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')  # 教师id
            # 教师详细对象
            obj = models.Teacher.objects.filter(pk=pk).first()

            ser = TeacherSerializer(instance=obj, many=False)
            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 1001
            ret['error'] = "获取教师信息失败"

        return Response(ret)
