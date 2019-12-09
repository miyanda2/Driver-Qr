from django import forms
from .models import Driver

class AddDriverForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name_of_driver'].widget.attrs.update({'class':'input-text required-entry'})
    #     self.fields['uploadedImage'].widget.attrs.update({'class':'input-text required-entry'})
    class Meta:
        model = Driver
        fields = (
            'name_of_driver',
            'uploadedImage'
        )