# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Movement


class MovementForm(forms.ModelForm):
	
	class Meta():

		model = Movement
		fields = ['movement','distance',]
		# widgets = {
		# 	'movement': forms.TextInput( attrs={'class':'form-control'}),
		# 	'distance': forms.TextInput( attrs={'class':'form-control'}),
 		# 		}