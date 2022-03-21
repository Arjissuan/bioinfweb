from django import forms
from .models import MultiMedia

# form for ability to upload images
class MultiMediaForm(forms.ModelForm):
    """"Form for multimedia"""
    class Meta:
        model = MultiMedia
        fields = ('title', 'image')