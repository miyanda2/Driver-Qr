from django import forms
from .models import Driver

class AddDriverForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_of_driver'].widget.attrs.update({'class':'form-control'})
        self.fields['email_address'].widget.attrs.update({'class':'form-control'})
        self.fields['address'].widget.attrs.update({'class':'form-control'})
        self.fields['city'].widget.attrs.update({'class':'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class':'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'class':'form-control','type':'date', "placeholder":"dd/mm/yyyy"})
        self.fields['educational_background'].widget.attrs.update({'class':'form-control'})
        self.fields['state_of_origin'].widget.attrs.update({'class':'form-control'})
        self.fields['local_government'].widget.attrs.update({'class':'form-control'})
        self.fields['blood_group'].widget.attrs.update({'class':'form-control'})
        self.fields['height'].widget.attrs.update({'class':'form-control'})
        self.fields['any_form_of_disability'].widget.attrs.update({'class':'form-control'})
        self.fields['nationality'].widget.attrs.update({'class':'form-control'})
        self.fields['next_of_kin'].widget.attrs.update({'class':'form-control'})
        self.fields['next_of_kin_phone_number'].widget.attrs.update({'class':'form-control'})
        self.fields['previous_number'].widget.attrs.update({'class':'form-control'})        
        self.fields['uploadedImage'].widget.attrs.update({'class':'custom-file-label', 'type':'file','id':'uploadedImage'})
    class Meta:
        model = Driver
        fields="__all__"
