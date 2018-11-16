from django.shortcuts import render,redirect
from .forms import registerForm
from rank.models import Registration,Point

def index(request):
	return render(request, 'index.html')

def event(request):
		return render(request, 'events.html')

def register_page(request):
	detailform = registerForm(request.POST or None)
	context ={"form" : detailform}
	if detailform.is_valid():
		fullname = detailform.cleaned_data.get('full_Name')
		year = detailform.cleaned_data.get('year')
		department = detailform.cleaned_data.get('address')
		phone = detailform.cleaned_data.get('phone')
		if request.method == "POST":
			event1 = request.POST['event1']
			event2 = request.POST['event2']
			event3 = request.POST['event3']
			event4 = request.POST['event4']
			Registration.objects.create(fullname=fullname,year=year,department=department,email=email,event_1=event1,event_2=event2,event_3=event3,event_4=event4)


	return render(request,"register.html",context)
