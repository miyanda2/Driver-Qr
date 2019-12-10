from django import forms
from .models import Driver

class AddDriverForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_of_driver'].widget.attrs.update({'class':'form-control'})
        self.fields['uploadedImage'].widget.attrs.update({'class':'custom-file-label', 'type':'file','id':'uploadedImage'})
    class Meta:
        model = Driver
        fields = (
            'name_of_driver',
            'uploadedImage'
        )