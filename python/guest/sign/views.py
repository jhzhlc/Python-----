# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将 session 信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        # if username == 'admin' and password == 'admin123':
        #     response = HttpResponseRedirect('/event_manage/')
        #     #response.set_cookie('user', username, 3600)  # 写cookie
        #     request.session['user'] = username # 将 session 信息记录到浏览器
        #     return response
        # # return HttpResponseRedirect('/event_manage/')
        # # response.set_cookie('passworld')

        else:
            return render(request, 'index.html', {'error': 'username or passworderror!'})
    # else:
        # return render(request, 'index.html', {'error': 'username or passworderror!'})

@login_required
def event_manage(request):
    # return render(request, "event_manage.html")
    # username = request.COOKIES.get('user', '')  # 读取浏览器 cookie
    username = request.session.get('user', '')  # 读取浏览器 session
    return render(request, "event_manage.html", {"user": username})
