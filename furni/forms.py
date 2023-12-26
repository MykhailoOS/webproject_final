from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'fname'})
    )
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'lname'})
    )
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'cols': '30', 'rows': '5'})
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')
