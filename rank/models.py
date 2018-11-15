from django.db import models

# Create your models here.
class Registration(models.Model):

	#Registation Table
	fullname = models.CharField(max_length=50)
	year = models.DecimalField(default =0,max_digits=1,decimal_places=0)
	department = models.CharField(max_length=50,null=True)
	email = models.CharField(max_length=50,null=True)
	event_1 = models.CharField(max_length=50,null=True)
	event_2 = models.CharField(max_length=50,null=True)
	event_3 = models.CharField(max_length=50,null=True)
	def __str__(self):
		return self.fullname

	def __unicode__(self):
		return self.fullname

class Result(models.Model):
	
	#Result Table
	event_name = models.CharField(max_length=50,default=None)
	first_prize = models.CharField(max_length=50,default=None)
	second_prize = models.CharField(max_length=50,default=None)
	third_prize = models.CharField(max_length=50,default=None) 

	def __str__(self):
		return self.event_name

	def __unicode__(self):
		return self.event_name

class Point(models.Model):
	
	#Points Table:
	year = models.CharField(max_length=50,default=None)
	points =  models.DecimalField(default =0,max_digits=3,decimal_places=0)

	def __str__(self):
		return self.year