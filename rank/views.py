from django.shortcuts import render
from . models import Point,Result, Registration
from . forms import RegistrationForm
import xlwt
from django.http import HttpResponse


# Create your views here

def index(request):
	return render(request, 'index.html')

def event(request):
		return render(request, 'events.html')



def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_data = form.save()
			return render(request, 'rank/register_success.html')
	else:
		form = RegistrationForm()
	return render(request, 'rank/register.html', {'form':form})


def score_view(request):
	
	queryset = Point.objects.all()
	context = {"score" : queryset }
	
	return render(request,"score.html",context)


#new
def result_view(request, name):

	queryset = Result.objects.all()
	context = {"result" : queryset }
	
	return render(request,"result_view.html",context)



def download_excel_data(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')

	#decide file name
	response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

	#creating workbook
	wb = xlwt.Workbook(encoding='utf-8')

	#adding sheet
	ws = wb.add_sheet("sheet1")

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names, you can use your own headers here
	columns = ['Name', 'Year', 'Department', 'Phone', 'Events' ]

	#write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	#get your data, from database or from a text file...
	data = get_data() #dummy method to fetch data.
	for my_row in data:
		row_num = row_num + 1
		ws.write(row_num, 0, my_row.name, font_style)
		ws.write(row_num, 1, my_row.start_date_time, font_style)
		ws.write(row_num, 2, my_row.end_date_time, font_style)
		ws.write(row_num, 3, my_row.notes, font_style)

	wb.save(response)
	return response