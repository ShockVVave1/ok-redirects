from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class RedirectsConfig(AppConfig):
    name = 'redirects'
    verbose_name = pgettext_lazy("ok:redirects", "Redirects")
