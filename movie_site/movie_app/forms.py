from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from django import forms


class UserSignupForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'login-username',
    }))

    password1 = forms.CharField(min_length=8, max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'login-password1',
    }))

    password2 = forms.CharField(min_length=8, max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'login-password2',
    }))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=500, widget=forms.TextInput(attrs={
        'margin-left': '150',
        'placeholder': 'Text',
    }))
    class Meta:
        model = Comment
        fields = ['comment']