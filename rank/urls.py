from django.urls import path, re_path
from . import views

urlpatterns = [
	path('register/', views.reg_closed, name='register_page'),
	path('events/',views.event, name='event'),
	path('',views.index, name='index'),
	#path('export/csv/', views.export_users_csv, name='export_users_csv'),
	path('team/',views.team, name='team'),
	path('results/',views.result_view,name='result')
]
