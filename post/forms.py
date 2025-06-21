from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from post.models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subheading','content', 'category', 'image']
    
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
                'subheading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a subheading'}),
                'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 200px;', 'placeholder': 'Enter content'}),
                'category': forms.Select(attrs={'class': 'form-control'}),
                'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            }
