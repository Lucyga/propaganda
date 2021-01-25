from django import forms
from django.contrib.auth.models import User

class FormRegistrazioneUser(forms.ModelForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'} ))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'} ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'} ))
    conferma_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'} ))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'conferma_password']
        
    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        conferma_password = self.cleaned_data['conferma_password']
        if password != conferma_password:
            raise forms.ValidationError('Le password non combaciano')
        return self.cleaned_data
        