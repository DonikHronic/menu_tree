from django.urls import path

from menu import views

urlpatterns = [
	path('', views.homepage, name='home'),
	path('<slug:slug>/', views.flatpage, name='flatpage')
]
