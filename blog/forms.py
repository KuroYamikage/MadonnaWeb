from django import forms
from blog.models import Blog

class BlogForms(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_content','blog_pic')
        widgets = {
            'blog_title': forms.TextInput(attrs={'class' : 'form-control'}),
            'blog_content':forms.Textarea(attrs={'class' : 'form-control'}),
            'blog_pic' : forms.ImageField(),
        }
        labels = {
            'blog_title':'Title',
            'blog_content':'Content',
            'blog_pic' : 'Upload Image'
        }