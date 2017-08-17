# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            response.set_cookie('user', username, 3600)  # 写cookie
            return response
        # return HttpResponseRedirect('/event_manage/')
        # response.set_cookie('passworld')

        else:
            return render(request, 'index.html', {'error': 'username or passworderror!'})
    # else:
        # return render(request, 'index.html', {'error': 'username or passworderror!'})


def event_manage(request):
    #return render(request, "event_manage.html")
    username = request.COOKIES.get('user', '')  # 读取浏览器 cookie
    return render(request, "event_manage.html", {"user": username})



