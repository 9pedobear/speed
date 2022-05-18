from django import forms
from .models import Feedback


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(
                               attrs={'class': 'form-group', 'placeholder': 'Search'}),)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'massage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-group', 'placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-group', 'placeholder': 'Phone'}),
            'massage': forms.Textarea(attrs={'class': 'form-group', 'placeholder': 'Message'}),
        }

# class FeedbackForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(
#                                attrs={'class': 'form-group', 'placeholder': 'Name'}),)
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-group', 'placeholder': 'Email'}),)
#     phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-group', 'placeholder': 'Phone'}))
#     massage = forms.Field(widget=forms.Textarea(attrs={'class': 'form-group', 'placeholder': 'Message'}),)