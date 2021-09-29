from django.shortcuts import render


def homepage(request):
	return render(request, 'index.html')


def flatpage(request, slug):
	context = {}
	return render(request, 'flatpages.html', context)
