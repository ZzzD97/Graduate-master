from django.db import models

# Create your models here.
from django.db import models

from utils.models import CommonModel
from teacher.models import Teacher, CollegeInfo


class CourseBaseInfo(CommonModel):
    u"""课程基本信息表，课程编号是主码"""
    cid = models.CharField(
        max_length=10, primary_key=True, unique=True, verbose_name=u"课程号")
    name = models.CharField(max_length=50, unique=True, verbose_name=u"课程名称")
    course_prop = models.CharField(
        max_length=2, null=True, verbose_name=u"课程性质", help_text=u"必修/限选/任选/校选")
    credit = models.FloatField(verbose_name=u"学分")
    study_hour = models.FloatField(default=0, verbose_name=u"总学时")
    cteacher = models.ManyToManyField(Teacher, verbose_name=u"开课老师")
    college = models.ForeignKey(CollegeInfo, null=True, on_delete=models.PROTECT, verbose_name=u"管理单位")

    def __str__(self):
        return "BaseCourse(%s)" % self.cid

    def GetCourseName(self):
        return "BaseCourse(%s)" % self.name


""" def GetCourseProp(self):
     #得到课程属性（任选/非任选)
     prop_list = [u"校选", u"非任选", u"任选"]
     cp = self.course_prop
     try:
         return prop_list[int(cp)]
     except:
         return u"未知(%s)" % cp
"""
