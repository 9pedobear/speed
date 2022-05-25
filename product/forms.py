from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class EmailForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput())
    content = forms.CharField(label='Тема', widget=forms.Textarea())








class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.PasswordInput()



class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')





class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(
                               attrs={'class': 'form-group', 'placeholder': 'Search'}),)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'massage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-group', 'placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-group', 'placeholder': 'Phone'}),
            'massage': forms.Textarea(attrs={'class': 'form-group', 'placeholder': 'Message'}),
        }

class FeedbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
                               attrs={'class': 'form-group', 'placeholder': 'Name'}),)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-group', 'placeholder': 'Email'}),)
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-group', 'placeholder': 'Phone'}))
    massage = forms.Field(widget=forms.Textarea(attrs={'class': 'form-group', 'placeholder': 'Message'}),)