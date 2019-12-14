from django import forms
from .models import Driver,FieldNumber

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


class AddFieldNumber(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state_of_issuance'].widget.attrs.update({'class':'form-control'})
        self.fields['class_of_liscense'].widget.attrs.update({'class':'form-control'})
        self.fields['number_of_replacement'].widget.attrs.update({'class':'form-control'})
        self.fields['license_of_number'].widget.attrs.update({'class':'form-control'})
        self.fields['chassess_number'].widget.attrs.update({'class':'form-control'})
        self.fields['plate_number'].widget.attrs.update({'class':'form-control'})
        self.fields['expiry_date'].widget.attrs.update({'class':'form-control'})
        self.fields['flag'].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = FieldNumber
        exclude=("driver",)
