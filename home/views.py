from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

# Importing Models

# Create your views here.
def home(request):
	title = 'JSG - Home page'
	context = {
	'title':title
	}
	return render(request, 'home/home.html', context)

def index(request):

	title = 'JSG - Home page'
	context = {
	'title':title
	}
	return render(request, 'home/home.html', context)

def about(request):
	return render(request, 'home/about.html')




# def register(request):
# 	if request.method == "POST":
# 		forms = Register(request.POST)

# 		if forms.is_valid():
# 			f_name = forms.cleaned_data["first_name"]
# 			l_name = forms.cleaned_data["last_name"]
# 			em = forms.cleaned_data["email"]
# 			num = forms.cleaned_data["phone"]
# 			user = Users(
# 				first_name=f_name,
# 				last_name=l_name,
# 				email=em,
# 				phone=num
# 				)
# 			user.save()
			
		
# 		else:
# 			form = Register()
	
# 	forms = Register()
# 	title = "Join now"
	
# 	context = {
# 	'title':title,
# 	'forms':forms,
# 	}
# 	return render(request, 'home/join.html', context)

# Test cases not to be used in production
# def test(request, id):
#     latest_user = Users.objects.order_by('first_name')[:5]
#     finder = Users.objects.get(id=id)
#     context = {
#     'latest_user':latest_user,
#     'finder':finder,
#     }
#     return render(request, 'home/test.html', context)

# def testvar(request,test_var):
# 	return HttpResponse(f"hello:{test_var}")

# This part is catching error from objects not in DB
# def errortesting(request):
#     usr = get_object_or_404(Users, pk=first_name)
#     return render(request, 'home/test.html', {'usr': usr})