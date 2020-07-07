from django.contrib import admin

from djangocms_github.forms import CredentialsAdminForm, OrganisationAdminForm, RepositoryAdminForm
from djangocms_github.models import Credentials, OrganisationPluginModel, RepositoryPluginModel


class CredentialsAdmin(admin.ModelAdmin):
    list_display = ["username", ]
    search_fields = ("username",)
    form = CredentialsAdminForm


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ("name",)
    form = OrganisationAdminForm


class OrganisationInlineAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ("name",)
    form = OrganisationAdminForm


class RepositoryAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]
    form = RepositoryAdminForm
    inline = [OrganisationAdmin, ]


admin.site.register(Credentials, CredentialsAdmin)
admin.site.register(OrganisationPluginModel, OrganisationAdmin)
admin.site.register(RepositoryPluginModel, RepositoryAdmin)
