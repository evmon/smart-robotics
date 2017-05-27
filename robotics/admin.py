# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Message, TemperatureBeforeMovement, Movement, Request

# Register models
admin.site.register(Movement)
admin.site.register(Message)
admin.site.register(Request)
admin.site.register(TemperatureBeforeMovement)