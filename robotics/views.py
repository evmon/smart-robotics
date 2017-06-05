# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db import connection
from django.views.generic import ListView, CreateView
from django.http import HttpResponseRedirect

from .models import PostRequest, SimpleMovement, CoordinatedMovement
from .forms import SimpleMovementForm, CoordinatedMovementForm


class List(ListView):
    
    context_object_name = 'list'
    queryset = PostRequest.objects.order_by('-id')[0:30]


class Simple(CreateView):

	model = SimpleMovement
	form_class = SimpleMovementForm
	success_url= '/control/simple/'

	def form_valid(self, form):

		if 'def' in self.request.POST: 
			# <input type="submit" name="def" value="Default" >
			SimpleMovement.objects.create(
				finger = self.request.POST['finger'],
				distance = 0,
				)
			
		elif 'ok' in self.request.POST: 
			# <input type="submit" name="ok" value="Default" >
			SimpleMovement.objects.create(
				finger = self.request.POST['finger'],
				distance=self.request.POST['distance'],
				)
			
		return HttpResponseRedirect(self.success_url)

		
class Coordinated(CreateView):

	model = CoordinatedMovement
	form_class = CoordinatedMovementForm
	success_url= '/control/coordinated/'

	def form_valid(self, form):

		if 'def' in self.request.POST:
			# <input type="submit" name="def" value="Default" >
			CoordinatedMovement.objects.create(
				finger = self.request.POST['movement'],
				distance = 0,
				)
			
		elif 'ok' in self.request.POST: 
			# <input type="submit" name="ok" value="Default" >
			CoordinatedMovement.objects.create(
				finger = self.request.POST['movement'],
				distance=self.request.POST['distance'],
				)
			
		return HttpResponseRedirect(self.success_url)