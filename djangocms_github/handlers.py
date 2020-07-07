import logging
import requests
from urllib.parse import urljoin

from django.apps import apps

from djangocms_github.constants import github_token

logger = logging.getLogger(__name__)


class AbstractAPIHandler:
    url = apps.get_app_config("djangocms_github").github_api_url

    class Meta:
        abstract = True

    def fetch_results(self, **kwargs):
        try:
            response = requests.get(url=self.url, params=kwargs, headers={'Authorization': github_token})
            response.raise_for_status()
            return response
        except Exception as e:
            logger.error(f"Error {e} occured when connecting to Github API")


class OrganisationAPIHandler(AbstractAPIHandler):
    def fetch_results(self, organisation):
        self.url = urljoin(self.url, f"orgs/{organisation}")
        return super(OrganisationAPIHandler, self).fetch_results()

    def get_plugin_fields(self, organisation):
        try:
            json = self.fetch_results(organisation).json()
        except AttributeError:
            return {}

        return {
            "name": json.get("name", ""), "blog": json.get("blog", ""),
            "html_url": json.get("html_url", ""), "description": json.get("description", "")
        }

    def check_organisation_exists(self, organisation_name):
        if self.fetch_results(organisation_name):
            return True
        else:
            False


class RepositoryAPIHandler(AbstractAPIHandler):
    def fetch_results(self, organisation, repo):
        self.url = urljoin(self.url, f"repos/{organisation}/{repo}")
        return super(RepositoryAPIHandler, self).fetch_results()

    def get_plugin_fields(self, organisation, repo):
        json = self.fetch_results(organisation, repo).json()
        return {
            "name": json.get("name", ""), "blog": json.get("blog", ""),
            "html_url": json.get("html_url", ""), "description": json.get("description", "")
        }

    def check_value_exists(self, organisation, repo_name):
        if self.fetch_results(organisation.name, repo_name):
            return True
        else:
            False
