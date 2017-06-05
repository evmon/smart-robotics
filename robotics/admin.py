# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Message, SimpleMovement, CoordinatedMovement, PostRequest

# Register models
admin.site.register(SimpleMovement)
admin.site.register(CoordinatedMovement)
admin.site.register(Message)
admin.site.register(PostRequest)
# admin.site.register(TemperatureBeforeMovement)