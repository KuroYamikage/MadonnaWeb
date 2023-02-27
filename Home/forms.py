from django import forms
<<<<<<< HEAD
from Home.models import Gallery

""" class GalleryForm(model) """
=======
from blog.models import Gallery

class GalleryForm(forms.ModelForm):
   
   class Meta:
    model = Gallery
    fields = [
        'galleryTitle',
        'galleryPic',
        'galleryTag',
    ]
>>>>>>> Reservation



