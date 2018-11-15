from django import forms
from django.contrib.auth import get_user_model
from rank.models import Registration

class registerForm(forms.Form):
	#registration form
	full_Name = forms.CharField(widget=forms.TextInput(attrs={}))
	year = forms.IntegerField(widget=forms.NumberInput(attrs={}))
	department = forms.CharField(widget=forms.TextInput(attrs={}))
	email_ID = forms.CharField(widget=forms.TextInput(attrs={}))
	
	def clean(self):
		fullname = self.cleaned_data.get('fullname')
		year = self.cleaned_data.get('year')
		email = self.cleaned_data.get('email')
		qs = Registration.objects.filter(fullname=fullname,year=year,email=email)
		if qs.exists():
			raise forms.ValidationError("Participant already registered !")
		
	
