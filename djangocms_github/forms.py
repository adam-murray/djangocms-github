from django import forms

from djangocms_github.handlers import OrganisationAPIHandler, RepositoryAPIHandler
from djangocms_github.models import (
    Credentials,
    OrganisationPluginModel,
    RepositoryPluginModel,
)


class CredentialsAdminForm(forms.ModelForm):
    """
    Add check that ensures credentials are valid with github
    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Credentials
        fields = ("username", "password")


class OrganisationAdminForm(forms.ModelForm):
    name = forms.CharField(max_length=255)

    class Meta:
        model = OrganisationPluginModel
        fields = ("name", )

    def clean(self):
        """
        Ensure that organisation exist by hitting the Github API and ensuring response code 200
        """
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        api_handler = OrganisationAPIHandler()
        if api_handler.check_organisation_exists(name):
            return cleaned_data
        else:
            raise forms.ValidationError(
                "Could not verify that organisation exists, please ensure valid organisation selected"
            )


class RepositoryAdminForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    organisation = forms.ModelChoiceField(queryset=OrganisationPluginModel.objects.all())

    class Meta:
        model = RepositoryPluginModel
        fields = ("name", )

    def clean(self):
        """
        Ensure that organisation exist by hitting the Github API and ensuring response code 200
        """
        cleaned_data = super().clean()
        repo_name = cleaned_data.get("name")
        organisation = cleaned_data.get("organisation")
        print(organisation)
        print(repo_name)
        api_handler = RepositoryAPIHandler()
        if api_handler.check_value_exists(organisation, repo_name):
            return cleaned_data
        else:
            raise forms.ValidationError(
                "Could not verify that repository exists, please ensure valid repository selected"
            )
