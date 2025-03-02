from django import forms
from django.core.exceptions import ValidationError
from .models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Enter assword again', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number')

    def clean_password(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 != password2:
            return ValidationError("Enterned passwords is not similar")
        

    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if user:
            user.save()
        return user 
    