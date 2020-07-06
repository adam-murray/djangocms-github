from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_github.handlers import OrganisationAPIHandler
from djangocms_github.models import GithubPluginModel, OrganisationPluginModel, RepositoryPluginModel


@plugin_pool.register_plugin
class GithubPlugin(CMSPluginBase):
    model = GithubPluginModel
    render_template = "djangocms_github/plugins/github_feed.html"
    change_form_template = "djangocms_github/plugins/github_changeform.html"

    def render(self, context, instance, placeholder):
        context = super(GithubPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class OrganisationPlugin(CMSPluginBase):
    model = OrganisationPluginModel
    render_template = "djangocms_github/plugins/github_orgnisation.html"
    change_form_template = "djangocms_github/plugins/github_changeform.html"
    read_only = True

    def render(self, context, instance, placeholder):
        context = super(OrganisationPlugin, self).render(context, instance, placeholder)
        api_handler = OrganisationAPIHandler()
        fields = api_handler.get_plugin_fields(instance.name)
        print(fields)
        if fields:
            for field in fields:
                context[field] = fields[field]
        print(context)
        return context


@plugin_pool.register_plugin
class RepositoryPlugin(CMSPluginBase):
    model = RepositoryPluginModel
    render_template = "djangocms_github/plugins/github_repo.html"
    read_only = True

    def render(self, context, instance, placeholder):
        context = super(RepositoryPlugin, self).render(context, instance, placeholder)
        return context
