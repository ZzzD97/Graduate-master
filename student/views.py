from rest_framework.response import Response
from course import models
from rest_framework.views import APIView
# Create your views here.
from rest_framework import serializers, generics
from rest_framework import mixins, viewsets
from student import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentInfo
        fields = "__all__"



class StudentEdit(mixins.ListModelMixin,  # 表示可以在Postman 类似的软件中只能查找所有数据
                  viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,  # 表示可以在Postman类似的软件中只能查找单一数据
                  mixins.UpdateModelMixin,  # 表示可以在Postman类似的软件中更新数据
                  mixins.DestroyModelMixin,  # 表示可以在Postman类似的软件中删除数据
                  mixins.CreateModelMixin):  # 表示可以在Postman类似的软件中创建数据

    # 查询所有信息
    queryset = models.StudentInfo.objects.all()
    # 序列化
    serializer_class = StudentSerializer




class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        """
        学生详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')  # 课程id
            # 课程详细对象
            obj = models.StudentInfo.objects.filter(pk=pk).first()

            ser = StudentSerializer(instance=obj, many=False)
            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 1001
            ret['error'] = "获取学生信息失败"

        return Response(ret)
