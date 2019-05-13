from django.db import models

# Create your models here.
from utils.models import CommonModel


class CollegeInfo(CommonModel):
    u"""二级学院信息表"""
    code = models.CharField(max_length=5, unique=True, verbose_name=u"学院编号")
    name = models.CharField(max_length=50, verbose_name=u"学院名称")
    abbr_name = models.CharField(max_length=20, null=True, verbose_name=u"学院简称")

    def __str__(self):
        return "%s college" % self.code


class Teacher(CommonModel):
    u"""教师名单"""
    tid = models.CharField(max_length=15, unique=True, verbose_name=u"教师编号")
    name = models.CharField(max_length=50, verbose_name=u"姓名")
    college = models.ForeignKey(CollegeInfo, null=True, on_delete=models.PROTECT, verbose_name=u"学院")
    worktype = models.CharField(max_length=1, verbose_name=u"职工类别")  # ‘1’：普通教师，‘2’：管理教师
    phone = models.CharField(
        max_length=15, unique=True, null=True, verbose_name=u"电话号码")

    def __str__(self):
        return "%s tid" % self.tid

    def __unicode__(self):
        return "%s name" % self.name
