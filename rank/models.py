from django.db import models

# Create your models here.

EVENTS=(
('KADHAPRASANGAM'),
('MONOACT'),
('WESTERN SOLO'),
('MAPPILAPATTU'),
('MIMICRY'),
('NAADODINIRTHAM'),
('OTTANTHULLAL'),
('BHARATHANATYAM'),
('MOHINIYATTAM'),
('SPEECH ENGLISH'),
('SPEECH MALAYALAM'),
('SPEECH HINDI'),
('VIOLINE'),
('VEENA'),
('ORGAN'),
('THABALA'),
('GUITAR'),
('MRITHANGAM'),
('KAVITHA MALAYALAM'),
('POEM ENGLISH'),
('POEM HINDI'),
('POEM ARABIC'),
('POEM SANSKRIT'),
('LIGHT MUSIC'),
('CLASSICAL MUSIC'),
)
class Registration(models.Model):

	#Registation Table
	fullname = models.CharField(max_length=50)
	year = models.DecimalField(default =0,max_digits=1,decimal_places=0)
	department = models.CharField(max_length=50,null=True)
	phone = models.CharField(max_length=12,null=True)
	event_1 = models.CharField(max_length=50,choices=EVENTS, default='KADHAPRASANGAM')
	event_2 = models.CharField(max_length=50,choices=EVENTS, default='KADHAPRASANGAM')
	event_3 = models.CharField(max_length=50,choices=EVENTS, default='KADHAPRASANGAM')
	event_4 = models.CharField(max_length=50,choices=EVENTS, default='KADHAPRASANGAM')
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
