from django.http import HttpResponse
from django.shortcuts import render
from myd.sample.testdb import _testdb, _show_db_usr


def _HttpResponse(request) -> HttpResponse:
    return HttpResponse('Hi')


def _render(request) -> HttpResponse:
    return render(request=request,
                  template_name='hello.html',
                  context={
                      'name': 'kkkk',
                      'condition': True,
                      'iter': [i for i in range(9)]
                  }
                  )


def _extend(request) -> HttpResponse:
    return render(request=request,
                  template_name='extend.html',
                  context={'name': 'qwerasd', }
                  )


def _shortcut(request) -> HttpResponse:
    return render(request,'folder/shortcut.html',{'foo':['admin','hr','render','extend','testdb_insert','showdbname']})