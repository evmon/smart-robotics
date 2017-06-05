# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


SIMPLE_CHOICES = (
	
            ('Thumb finger', 'Thumb finger'),
            ('Index finger', 'Index finger'),
            ('Middle finger', 'Middle finger'),
            ('Ring finder', 'Ring finder'),
            ('Little finger', 'Little finger'),
	)

COORDINATED_CHOICES = (
			('Take', 'Take'),
			('Let go', 'Let go'),
			('Move', 'Move'),
	)


@python_2_unicode_compatible
class SimpleMovement(models.Model):
	"""
	Model for SimpleMovement.
	- finger
	- distance
	- time
	"""
	finger = models.CharField(
		max_length=50, 
		verbose_name='Finger', 
		choices=SIMPLE_CHOICES,
		default='Thumb finger',
        )
	
	distance = models.IntegerField(
    	verbose_name="Distance",
    	default=0,
    	validators=[
            MinValueValidator(0),
            MaxValueValidator(174)
		])
	time = models.DateTimeField(default=timezone.now)
	
	def __str__(self): 
		return '{0} {1} ({2})'.format(self.time, self.finger, self.distance )
   

@python_2_unicode_compatible
class CoordinatedMovement(models.Model):
	"""
	Model for CoordinatedMovement.
	- movement
	- distance
	- time
	"""
	movement = models.CharField(
		max_length=50, 
		verbose_name='Movement', 
		choices=COORDINATED_CHOICES,
		default='Take',
        )
	
	distance = models.IntegerField(
    	verbose_name="Distance",
    	default=0,
    	validators=[
            MinValueValidator(0),
            MaxValueValidator(174)
		])
	time = models.DateTimeField(default=timezone.now)
	
	def __str__(self): 
		return '{0} {1} ({2})'.format(self.time, self.movement, self.distance )


# @python_2_unicode_compatible
# class TemperatureBeforeMovement(models.Model):
# 	"""
# 	Model for Temperature Before SimpleMovement.
# 	- temperature
# 	- time
# 	"""

# 	temperature_before_movement = models.OneToOneField(
#         SimpleMovement,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
# 	temperature = models.IntegerField(
# 		verbose_name="Temperature",
# 		validators=[
#             MinValueValidator(-150),
#             MaxValueValidator(150)
# 		])

# 	time = models.DateTimeField(default=timezone.now)

# 	def __str__(self):
# 		return 'Temperature before movement: {0} °C for {1}'.format(self.temperature, self.temperature_before_movement.movement)


@python_2_unicode_compatible
class Message(models.Model):
	"""
	Model for Message.
	- msg
	- text
	- time
	"""

	msg = models.CharField(max_length=50, verbose_name='Message')
	text = models.TextField()
	time = models.DateTimeField(default=timezone.now)
        
	def __str__(self):
   		return '{0} | {1} - {2}'.format(self.time, self.msg, self.text )



@python_2_unicode_compatible
class PostRequest(models.Model):
    """ Model request that are stored by middleware
        :param str text: includes id and 100 request symbol

    """
    request = models.TextField()

    def __str__(self):
        text = '{}: {}'.format(self.id, "%.100s" % self.request)
        return text
