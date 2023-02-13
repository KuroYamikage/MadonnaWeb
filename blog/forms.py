from django import forms
from blog.models import Blog

class BlogForms(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_content')
        widgets = {
            'blog_title': forms.TextInput(attrs={'class' : 'form-control'}),
            'blog_content':forms.Textarea(attrs={'class' : 'form-control'})
        }
        labels = {
            'blog_title':'title',
            'blog_content':'content'
        }