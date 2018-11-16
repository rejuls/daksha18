from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class Registration(models.Model):

	EVENTS_CHOICES = (
	('kadaprasangham', 'KADHAPRASANGAM'),
	('monoact', 'MONOACT'),
	('western_solo', 'WESTERN SOLO'),
	('mappila', 'MAPPILAPATTU'),
	('mimicry', 'MIMICRY'),
	('naadoodinritham', 'NAADODINIRTHAM'),
	('ottamthulla', 'OTTANTHULLAL'),
	('bharathanatyam', 'BHARATHANATYAM'),
	('mohiniyattam', 'MOHINIYATTAM'),
	('speech_eng', 'SPEECH ENGLISH'),
	('speech_mal', 'SPEECH MALAYALAM'),
	('speech_hin', 'SPEECH HINDI'),
	('violin', 'VIOLIN'),
	('veena', 'VEENA'),
	('organ', 'ORGAN'),
	('thabala', 'THABALA'),
	('guitar', 'GUITAR'),
	('mrithangam', 'MRITHANGAM'),
	('kavitha_mal', 'KAVITHA MALAYALAM'),
	('poem_eng', 'POEM ENGLISH'),
	('poem_hin', 'POEM HINDI'),
	('poem_arab', 'POEM ARABIC'),
	('poem_sanskrit', 'POEM SANSKRIT'),
	('lightmusic','LIGHT MUSIC'),
	('classic_music','CLASSICAL MUSIC'))

	#Registation Table
	full_name = models.CharField(max_length=50)
	year = models.DecimalField(default =0,max_digits=1,decimal_places=0)
	department = models.CharField(max_length=50,null=True)
	phone = models.CharField(max_length=12,null=True)
	events = MultiSelectField(choices=EVENTS_CHOICES, max_choices=4, default='KADHAPRASANGAM')
	
	def __str__(self):
		return self.fullname

	def __unicode__(self):
		return self.full_name

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
