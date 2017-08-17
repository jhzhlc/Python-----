# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from sign.models import Event,Guest

# Register your models here.
admin.site.register(Event)
admin.site.register(Guest)
# Register your models here.
class EventAdmin(admin.ModelAdmin):

    list_display = ['name', 'status', 'start_time','id']
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone','email','sign','create_time','event']
    admin.site.register(Event,EventAdmin)
    admin.site.register(Guest,GuestAdmin)