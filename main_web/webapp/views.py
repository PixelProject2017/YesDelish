from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	return render(request, 'web_content/index.html')

def sign_up(request):
    return render(request, 'web_content/hello.html')