from django import forms

# from .models import SignUp

class ContactForm(forms.Form):
	nombre_Comleto = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje = forms.CharField()
	Fecha = forms.DateField()