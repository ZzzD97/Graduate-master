from django.db import models
from utils.models import CommonModel

# Create your models here.
from course.models import CollegeInfo


class GradeInfo(models.Model):
    grade = models.CharField(max_length=4, verbose_name=u"年级")


class MajorInfo(models.Model):
    mid = models.CharField(max_length=5, verbose_name=u"专业编号")
    mname = models.CharField(max_length=50, null=True, verbose_name=u"专业名称")
    mcollege = models.ForeignKey(CollegeInfo, on_delete=models.PROTECT, verbose_name=u"开设学院")

    def __str__(self):
        return "%s major" % self.mid


class ClassInfo(models.Model):
    clid = models.CharField(max_length=5, primary_key=True, verbose_name=u"班级编号")
    clgrade = models.ForeignKey(GradeInfo, on_delete=models.PROTECT, null=True, verbose_name=u"年级")
    clmajor = models.ForeignKey(to='MajorInfo', on_delete=models.PROTECT, verbose_name=u"专业")

    def __str__(self):
        return "%s class" % self.clid


class StudentInfo(CommonModel):
    sid = models.CharField(max_length=50, primary_key=True, verbose_name=u"学号")
    sname = models.CharField(max_length=50, verbose_name=u"学生姓名")
    sgrade = models.ForeignKey(GradeInfo, on_delete=models.PROTECT, verbose_name=u"学生所属年级")
    sclass = models.ForeignKey(ClassInfo, null=True, on_delete=models.PROTECT, verbose_name=u"学生所属班级")
    smajor = models.ForeignKey(MajorInfo, null=True, on_delete=models.PROTECT, verbose_name=u"学生专业")
    scollege = models.ForeignKey(CollegeInfo, max_length=50, null=True, on_delete=models.PROTECT,
                                 verbose_name=u"学生所属学院")
    scomment = models.CharField(max_length=128, null=True, verbose_name=u"备注")

    def __str__(self):
        return "%s college" % self.sid
