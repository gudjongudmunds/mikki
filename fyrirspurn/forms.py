from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nafn'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Netfang'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Símanúmer'}),
            'message': forms.Textarea(attrs={'placeholder': 'Fyrirspurnin þín'}),
        }