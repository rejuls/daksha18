from django.shortcuts import render
from .models import Point,Result
# Create your views here

def score_view(request):
	
	queryset = Point.objects.all()
	context = {"score" : queryset }
	
	return render(request,"score.html",context)


#new
def result_view(request, name):

	queryset = Result.objects.all()
	context = {"result" : queryset }
	
	return render(request,"result_view.html",context)
