from django.test import override_settings

from wagtailforms.urls import urlpatterns

from .test_case import AppTestCase


class UrlsTests(AppTestCase):
    @override_settings(WAGTAILFORMS_ADVANCED_SETTINGS_MODEL=None)
    def test_no_advanced_url_when_no_setting(self):
        self.reload_module("wagtailforms.urls")
        self.assertEqual(len(urlpatterns), 3)

    @override_settings(WAGTAILFORMS_ADVANCED_SETTINGS_MODEL="tests.ValidFormSettingsModel")
    def test_no_advanced_url_when_no_setting(self):
        self.reload_module("wagtailforms.urls")
        self.assertEqual(len(urlpatterns), 4)
