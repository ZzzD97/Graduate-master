from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models


class CommonModel(models.Model):
    is_valid = models.BooleanField(default=True, verbose_name=u"是否有效")
    is_deleted = models.BooleanField(default=False, verbose_name=u"是否已删除")

    class Meta:
        abstract = True


# class UserInfo(models.Model):
#     user_type_choice = {
#         (1,'管理员'),
#         (2,'教师'),
#         (3,'学生')
#     }
#     userid = models.CharField(max_length=10, primary_key=True, verbose_name=u"用户id")
#     username = models.CharField(max_length=20, verbose_name=u"用户姓名")
#     password = models.CharField(max_length=20, verbose_name=u"密码")
#     user_type = models.IntegerField(choices=user_type_choice, verbose_name=u"用户类型")