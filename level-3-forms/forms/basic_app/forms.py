from django import forms
from django.core import validators
from basic_app.models import Preorder

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError(
            'NAME NEEDS TO START WITH Z'
        )

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail:
            raise forms.ValidationError(
                'MAKE SURE EMAILS MATCH!'
            )

class PreorderForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    birthdate = forms.DateField(input_formats=['%d.%m.%Y'])

    class Meta():
        model = Preorder
        fields = '__all__' # ['name', 'email', 'birthdate']