from django import forms
from home.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", 
            "placeholder":"Enter the name"}),
            "age": forms.EmailInput(attrs={"class": "form-control", 
            "placeholder":"Enter the email"}),
            "message": forms.Textarea(attrs={"class": "form-control", 
            "placeholder":"Enter the message"})
        }