from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


class Credentials(models.Model):
    username = models.CharField(verbose_name=_("Github Username"), max_length=255)
    password = models.CharField(verbose_name=_("Password"), max_length=255)


class GithubPluginModel(CMSPlugin):
    credentials = models.ForeignKey(Credentials, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OrganisationPluginModel(CMSPlugin):
    name = models.CharField(verbose_name=_("Organisation Name"), max_length=255, blank=True)

    def __str__(self):
        return self.name


class RepositoryPluginModel(CMSPlugin):
    name = models.CharField(max_length=255)
    organisation = models.ForeignKey(OrganisationPluginModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
