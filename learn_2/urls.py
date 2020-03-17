"""learn_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql

account = ("localhost", "root", 'sjh920813', 'ss')
conn = pymysql.connect(*account)
cursor = conn.cursor()


def aj0(request):
    k = request.POST.get('title')
    print(k)
    if k :
        cursor.execute("insert into tmp values (%s)",[k])
        conn.commit()
    return HttpResponse('okokok')

def aj1(request):
    return render(request, 'hide.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post_ajax/', aj0),
    path('test_ajax_input/', aj1),

]
