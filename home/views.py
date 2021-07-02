from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404
from django.template import loader


# Importing Models

# Create your views here.
def index(request):

	

	title = 'JSG - Home page'
	context = {
	'title':title
	}
	return render(request, 'home/home.html', context)

def about(request):
	return render(request, 'home/about.html')

def test(request):
	return render(request, 'home/test.html')

def handler404(request, exception):
	return render(request,'home/404.html', status=404)



# This part is catching error from objects not in DB
# def errortesting(request):
#     usr = get_object_or_404(Users, pk=first_name)
#     return render(request, 'home/test.html', {'usr': usr})