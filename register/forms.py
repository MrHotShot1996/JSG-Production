from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re


# Number Validator
# validate_phone = RegexValidator(r'^(05)\d{9}$', 
# 	"must only be numbers", 
# 	"invalid number")

# Custom validators
def validate_phone(val):
	if not re.match(r'^(05)', val):
		raise ValidationError("Please start with '05'")

class Register(forms.Form):
	first_name = forms.CharField(label="First Name", max_length=20,)

	last_name = forms.CharField(label="Last Name", max_length=20)

	email = forms.EmailField(label="Email", 
		max_length=50,
		help_text="Johndoe@email.com")

	phone = forms.CharField(label="Phone",
		help_text="0555555555",
		max_length=10,
		min_length=10,
		validators=[validate_phone])
