from django import forms
from .models import Blog

class BlogPost(forms.ModelForm): #models.py 에 있는 Blog를 바탕으로 form을 만들기때문에 modelform임
    class Meta: #class 안에 또 클래스르 만드는것 Meta
        model = Blog
        fields = ['title', 'body']
