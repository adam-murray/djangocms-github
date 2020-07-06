import settings

from django.apps import AppConfig

from .constants import github_default_url


class GithubAppConfig(AppConfig):
    name = "djangocms_github"
    verbose_name = "DjangoCMS Github Feed"
    github_api_url = getattr(settings, "DJANGOCMS_GITHUB_API_URL", github_default_url)
