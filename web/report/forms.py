from django import forms
"""from django.contrib.auth.forms import UserCreationForm"""
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout,get_user_model
from . models import Topic


class SignUpForm(forms.ModelForm):
	class Meta:
		model = User
		"""password = forms.CharField(widget=forms.PasswordInput)"""
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

"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
"""
class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placeholder':'what is on your mind?'}), max_length=4000,help_text = 'Maximum length of the text is 4000')

    class Meta:
        model = Topic
        fields = ['subject', 'message']



















    

