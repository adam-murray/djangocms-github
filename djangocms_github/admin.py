from django.contrib import admin

from djangocms_github.forms import CredentialsAdminForm
from djangocms_github.models import Credentials


class CredentialsAdmin(admin.ModelAdmin):
    list_display = ["username",]
    form = CredentialsAdminForm


admin.site.register(Credentials, CredentialsAdmin)
