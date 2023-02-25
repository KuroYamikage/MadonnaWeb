from django import forms
from blog.models import Gallery

class GalleryForm(forms.ModelForm):
   
   class Meta:
    model = Gallery
    fields = [
        'galleryTitle',
        'galleryPic',
        'galleryTag',
    ]



