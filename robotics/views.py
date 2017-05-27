# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db import connection
from django.views.generic import ListView

from .models import Request


class List(ListView):
    
    context_object_name = 'list'
    queryset = Request.objects.all()[:20]