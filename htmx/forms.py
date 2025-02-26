from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Books 

class FormBooks(forms.ModelForm):
    title = forms.CharField(required=False, label=  _('Title'), widget=forms.TextInput(attrs={'class': 'clrtxt', 'placeholder':_('Title'), }))
    author= forms.CharField(required=False, label= _('Author') ,widget=forms.TextInput(attrs={'class': 'clrtxt', 'placeholder':_('Author'), }))
    price = forms.CharField(required=False, label= _('Price') ,widget=forms.TextInput(attrs={'class': 'clrtxt', 'placeholder':_('Price'),}))
    read = forms.BooleanField(required=False, label = _('Read'))

    class Meta:
        model = Books 
        fields = ['title', 'author','price', 'read']