from django import forms

from djangocms_github.models import Credentials


class CredentialsAdminForm(forms.ModelForm):
    """
    Add check that ensures credentials are valid with github
    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Credentials
        fields = ("username", "password")
