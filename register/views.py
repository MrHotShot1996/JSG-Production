from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from django.core.mail import send_mail, mail_admins
from .forms import Register
import os

# Importing Models
from .models import Users

# Create your views here.
def register(request):
	if request.method == "POST":
		forms = Register(request.POST)

		# If the form is valid
		if forms.is_valid():
			f_name = forms.cleaned_data["first_name"]
			l_name = forms.cleaned_data["last_name"]
			em = forms.cleaned_data["email"]
			num = forms.cleaned_data["phone"]
			user = Users(
				first_name=f_name,
				last_name=l_name,
				email=em,
				phone=num
				)
			user.save()
			# Saving name session
			request.session['f_name'] = f_name
			
			# User Mailing
			subject = f'Welcome to JSG {f_name}'
			message = 'Testing'
			from_email = os.environ.get('email_name')
			recipient_list = [em]

			user_mail = send_mail(
				subject,
				message,
				from_email,
				recipient_list,
				fail_silently = False,
				)

			# Admin Mailing
			subject = f'New member has joined the family {f_name}'
			message = ( f"Name: {f_name} {l_name}\n" 
						f"Email: {em}\n"
						f"Phone: {num}\n" 
					  )

			admin_mail = mail_admins(
				subject,
				message,
				fail_silently = False,
				)

			return redirect('success')

			
				
		# If the form is not valid
		else:
			context = {
				'forms':forms
					  }
			return render(request, 'register/register.html', context)
	
	forms = Register()
	title = "Join now"
	
	context = {
	'title':title,
	'forms':forms,
	}
	
	return render(request, 'register/register.html', context)

def success(request):
	# Rendering name session to the template
	welcome = request.session['f_name']

		
	context = {
		'welcome' : welcome
		}
	return render(request, 'register/success.html', context)






	