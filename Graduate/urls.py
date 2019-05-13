"""Graduate1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from student.views import StudentView, StudentEdit
from course.views import CourseView, CourseDetail
from teacher.views import TeacherView,TeacherEdit

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'student1', StudentEdit)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^(?P<version>[v1|v2]+)/course/(?P<pk>\d+)/$', CourseView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/student/(?P<pk>\d+)/$', StudentView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/teacher/(?P<pk>\d+)/$', TeacherView.as_view()),
    #url(r'^(?P<version>[v1|v2]+)/studentdetail/(?P<pk>[0-9]+)$', StudentEdit.as_view()),
    #url(r'^(?P<version>[v1|v2]+)/teacherdetail/(?P<pk>[0-9]+)$', TeacherEdit.as_view()),
    url(r'^(?P<version>[v1|v2]+)/coursedetail/(?P<pk>[0-9]+)$', CourseDetail.as_view()),

    path(r"login", obtain_jwt_token),
    url(r'^', include(router.urls))
]
urlpatterns += router.urls  # 这里表示添加定义的url
