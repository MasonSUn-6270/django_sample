# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpRequest
from TestModel.models import Test
from django.shortcuts import redirect, render


def _testdb(request: HttpRequest):
    print(request.COOKIES)
    if  request.method == "POST" and request.POST.get('poet'):
        k = request.POST['poet']
        test1 = Test(name=k)
        test1.save()
        return redirect('/testdb_insert')
    else:
        return render(request, 'insert.html')


def _show_db_usr(request):
    tar = ''
    foo = Test.objects.all()
    for i in foo:
        tar += str(i.id) + '  ' + i.name
    return HttpResponse("<p>数据添加成功！" + tar + "</p>")
