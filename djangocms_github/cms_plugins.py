from cms.plugin_base import CMSPluginBase

from djangocms_github.models import GithubPluginModel, RepositoryPluginModel


class GithubPlugin(CMSPluginBase):
    model = GithubPluginModel
    render_template = "djangocms_github/plugins/github_feed.html"
    change_form_template = "djangocms_github/plugins/github_change_form.html"


class RepositoryPlugin(CMSPluginBase):
    model = RepositoryPluginModel
    render_template = "djangocms_github/plugins/github_repo.html"

