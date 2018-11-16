from django.forms import ModelForm
from . models import Registration

class RegistrationForm(ModelForm):
	class Meta:
		model = Registration
		fields = ['full_name','year','department','phone','events']
		def __init__(self, *args, **kwargs):
			super(SampleClass, self).__init__(*args, **kwargs)
			self.fields['name'].widget.attrs['class'] = 'input--style-5'