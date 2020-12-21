from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
	return render(request, 'DEMOAPP/welcome.html')

def test(request):
	return render(request, 'DEMOAPP/test.html', {'sohel': 'dd'})

def brand(request):
	return render(request, 'DEMOAPP/brand.html')