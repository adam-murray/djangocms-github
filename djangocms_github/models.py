from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


class Credentials(models.Model):
    username = models.CharField(verbose_name=_("Github Username"), max_length=255)
    password = models.CharField(verbose_name=_("Password"), max_length=255)


class GithubPluginModel(CMSPlugin):
    credentials = models.ForeignKey(Credentials, on_delete=models.CASCADE)


class RepositoryPluginModel(CMSPlugin):
    container_plugin = models.ForeignKey(GithubPluginModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    html_url = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    updated_at = models.DateTimeField(null=True)
    fetched_at = models.DateTimeField(auto_now=True)

