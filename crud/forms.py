from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Detail


class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=255, 
        help_text=_("Password should be 9 characters minimum, contain at least one lowercase, uppercase, symbol and number. No whitespace allowed e.g., A1!.#laN87@Jp"), 
        widget=forms.PasswordInput
    )
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password")
        labels = {
            "first_name": _("First name"),
            "last_name": _("Last name"), 
            "email": _("Email"),
            "username": _("Username"),
            "password": _("Password")
        }
        widgets = {
            "password": forms.PasswordInput,
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error(
                "password", 
                ValidationError(
                    message=_("Password does not match confirm password"),
                    code="mismatch"
                )
            )
            self.add_error(
                "confirm_password", 
                ValidationError(
                    message=_("Confirm password does not match password"),
                    code="mismatch"
                )
            )


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ["phone", "dob", "married", "kids", "title", "duration"]
        labels = {
            "phone": _("Phone number"),
            "dob": _("Date of birth"),
            "duration": _("Contract Duration")
        }
        widgets = {
            "phone": forms.TextInput(attrs={
                "placeholder": "237xxxxxxxxx"
            }),
            "dob": forms.DateInput(attrs={
                "placeholder": "YYYY-MM-DD",
            }),
            "title": forms.TextInput(attrs={
                "placeholder": _("Network/Security Engineer")
            })
        }
