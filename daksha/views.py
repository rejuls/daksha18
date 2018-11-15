from django.shortcuts import render,redirect
from .forms import registerForm
from rank.models import Registration,Point

def index(request):
	return render(request, 'index.html')
        
def register_page(request):
	detailform = registerForm(request.POST or None)
	context ={"form" : detailform}		
	if detailform.is_valid():
		fullname = detailform.cleaned_data.get('full_Name')
		year = detailform.cleaned_data.get('year')
		department = detailform.cleaned_data.get('address')
		email = detailform.cleaned_data.get('email_ID')
		if request.method == "POST":
			event1 = request.POST['event1']
			event2 = request.POST['event2']
			event3 = request.POST['event3']
			Registration.objects.create(fullname=fullname,year=year,department=department,email=email,event_1=event1,event_2=event2,event_3=event3)
				
		
	return render(request,"register_page.html",context)