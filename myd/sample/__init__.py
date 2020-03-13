from django.http import HttpResponse
from django.shortcuts import render


def _HttpResponse(request):
    return HttpResponse('Hi')


def _render(request):
    return render(request=request,
                  template_name='hello.html',
                  context={
                      'name': 'kkkk',
                      'condition': True,
                      'iter': [i for i in range(9)]
                  }
                  )


def _extend(request):
    return render(request=request,
                  template_name='extend.html',
                  context={'name': 'qwerasd', }
                  )
