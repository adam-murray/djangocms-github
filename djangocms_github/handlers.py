import logging
import requests
from urllib.parse import urljoin

from django.apps import apps

logger = logging.getLogger(__name__)


class AbstractAPIHandler:
    print(dir(apps.get_app_config("djangocms_github")))
    url = apps.get_app_config("djangocms_github").github_api_url

    class Meta:
        abstract = True

    def fetch_results(self, **kwargs):
        try:
            response = requests.get(url=self.url, params=kwargs)
            response.raise_for_status()
            print(response.text)
            print(response.json)
            return response.json
        except Exception as e:
            logger.error(f"Error {e} occured when connecting to Github API")


class OrganisationAPIHandler(AbstractAPIHandler):
    def fetch_results(self, organisation):
        self.url = urljoin(self.url, f"orgs/{organisation}")
        return super(OrganisationAPIHandler, self).fetch_results()

    def get_plugin_fields(self, organisation):
        json = self.fetch_results(organisation)()
        return {
            "name": json.get("name", ""), "blog": json.get("blog", ""),
            "html_url": json.get("html_url", ""), "description": json.get("description", "")
        }


