from django import forms
from .models import Driver,FieldNumber
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

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
        exclude= ('user',)


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


# Seller Registration Form
class SignupForm(forms.ModelForm):
    full_name= forms.CharField(max_length=50)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    pwd1 = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Password')
    pwd2 = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Re-Enter Password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'class':'form-control mb-4', 'placeholder':'Enter Full Name'})
        self.fields['username'].widget.attrs.update({'class':'form-control mb-4', 'placeholder':'Enter Username'})
        self.fields['email'].widget.attrs.update({'class':'form-control mb-4','placeholder':'Enter Email'})
        self.fields['pwd1'].widget.attrs.update({'class':'form-control mb-4','placeholder':'Enter Password' })
        self.fields['pwd2'].widget.attrs.update({'class':'form-control mb-4','placeholder':'Retype Password' })

    class Meta:
        model = User
        fields = [ 
                'full_name', 
                'username',
                'email', 
                'pwd1', 
                'pwd2', 
                ]

    def clean_username(self):
        if 'username' in self.cleaned_data:
            try:
                User.objects.get(username=self.cleaned_data['username'])
            except User.DoesNotExist:
                return self.cleaned_data['username']
            else:
                raise forms.ValidationError(
                    'An account with this email already exists')

    def clean_pwd2(self):
        password1 = self.cleaned_data.get("pwd1")
        password2 = self.cleaned_data.get("pwd2")  
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['pwd1'])
            if commit:
                user.save()
            return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control mb-4','placeholder':'username'})
        self.fields['password'].widget.attrs.update({'class':'form-control mb-4','placeholder':'password'})


