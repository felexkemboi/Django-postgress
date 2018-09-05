from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout,get_user_model


class SignUpForm(forms.ModelForm):
	class Meta:
		model = User
		password = forms.CharField(widget=forms.PasswordInput)
		fields = [
			'username',
			'email',
			'password'
		]
	"""
	username = forms.CharField(max_length=30, required=False,)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')"""

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args,**kwargs):
    	username = self.cleaned_data.get('username')
    	password = self.cleaned_data.get('password')
    	user = authenticate(username = username,password=password)

    	if not user:
    		raise forms.validationError("This user does not exists")

    	if not user.check_password(password):
    		raise forms.validationError("Incorrect password")
    	if not user.is_active:
    		raise forms.validationError("This user is no longer active")
    	return super(LoginForm,self).clean(*args,**kwargs)
		



