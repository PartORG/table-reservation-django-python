# forms
from django import forms

class SendEmail(forms.Form):
	name = forms.CharField(label="Name", max_length=200)
	email = forms.EmailField(required = True)	