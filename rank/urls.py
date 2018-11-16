from django.urls import path, re_path
from .import views

urlpatterns = [
	path('register/', views.register_page, name='register_page'),
	path('events/',views.event, name='event'),
	path('',views.index, name='index'),
]