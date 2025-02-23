from django import forms

from .models import Books 

class FormBooks(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'clrtxt', 'placeholder':'Title'}))
    author= forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'clrtxt', 'placeholder':'Author'}))
    price = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'clrtxt', 'placeholder':'Price'}))

    class Meta:
        model = Books 
        fields = ['title', 'author','price', 'read']