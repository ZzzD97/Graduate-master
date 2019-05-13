from django.db import models

# Create your models here.
from teacher.models import Teacher
from utils.models import CommonModel
from course.models import CourseBaseInfo
from student.models import ClassInfo, GradeInfo, MajorInfo


class ClassroomInfo(models.Model):
    u"""教室信息"""
    ccode = models.CharField(max_length=5, unique=True, verbose_name=u"教室编号")
    capacity = models.CharField(max_length=3, verbose_name=u"教室容量")

    def __str__(self):
        return "%s classroom" % self.ccode


class CourseArrange(CommonModel):
    u"""所需安排课程"""
    cid = models.ForeignKey(CourseBaseInfo, on_delete=models.PROTECT, verbose_name=u"课程编号")
    cname = models.ForeignKey(CourseBaseInfo, related_name='coursearrange_coursebaseinfo', on_delete=models.PROTECT,
                              verbose_name=u"课程名称")
    cclass = models.ForeignKey(ClassInfo, on_delete=models.PROTECT, verbose_name=u"对应班级")
    cmajor = models.ForeignKey(MajorInfo, on_delete=models.PROTECT, verbose_name=u"对应专业")


class CourseTable(CommonModel):
    u"""课表"""
    cclass = models.ForeignKey(ClassInfo, on_delete=models.PROTECT, verbose_name=u"班级")
    cgrade = models.ForeignKey(GradeInfo, on_delete=models.PROTECT, verbose_name=u"开课年级")
    cid = models.ForeignKey(CourseBaseInfo, on_delete=models.PROTECT, verbose_name=u"课程编号")
    cteacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name=u"上课老师")
    workday = models.CharField(max_length=6, verbose_name=u"上课时间")
    time = models.CharField(max_length=25, verbose_name=u"上课具体时间")
    classroom = models.ForeignKey(ClassroomInfo, on_delete=models.PROTECT, verbose_name=u"教室")
