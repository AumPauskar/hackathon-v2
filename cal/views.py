from django.shortcuts import render
from django.http import HttpResponse
from . models import Cal

# Create your views here.
def index(request):
	cals = Cal.objects.all()
	# return HttpResponse('Hello world')
	return render(request, 'index.html', {'cals': cals})