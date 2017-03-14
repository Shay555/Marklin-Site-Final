from django import forms
from .models import Pictures


class ImagePostForm(forms.ModelForm):
    class Meta:
        model = Pictures
        fields = ('author', 'title', 'image')

