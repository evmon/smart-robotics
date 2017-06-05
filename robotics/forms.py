# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import CoordinatedMovement, SimpleMovement


class SimpleMovementForm(forms.ModelForm):
	
	class Meta():
		
		model = SimpleMovement
		fields = ['finger','distance',]
		widgets = {
			'finger': forms.Select(
				
				attrs={
				'style':"padding: 10px 55px; font-family: 'Open Sans', sans-serif; font-size: 1.5em; ",
				}),

			'distance': forms.TextInput( 
				attrs={
				'style':"margin-top: 20px; width: 23px; float:right; text-align: center; ",
			 	'value':"0", 
			 	'type':"text1", 
			 	'id':"text1",}),
 			}


class CoordinatedMovementForm(forms.ModelForm):
	
	class Meta():
		
		model = CoordinatedMovement
		fields = ['movement','distance',]
		widgets = {
			'movement': forms.Select(
				
				attrs={
				'style':" padding: 10px 55px; font-family: 'Open Sans', sans-serif;  font-size: 1.5em;",}),

			'distance': forms.TextInput( attrs={
				'style':"margin-top: 20px; width: 23px; float:right; text-align: center;",
			 	'value':"0", 
			 	'type':"text1", 
			 	'id':"text1",}),
 			}