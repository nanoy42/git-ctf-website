from django import forms
from django.core.exceptions import ValidationError


class CTFForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=255)
    token = forms.CharField(label="CTF token", max_length=255)

    def clean_token(self):
        clean_token = self.cleaned_data["token"]
        if clean_token != "ctf-token":
            raise ValidationError("CTF token is invalid")
        return clean_token
