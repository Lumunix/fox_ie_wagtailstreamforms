from django.urls import path

from wagtailforms import views
from wagtailforms.utils.loading import get_advanced_settings_model

SettingsModel = get_advanced_settings_model()


urlpatterns = [
    path("<int:pk>/copy/", views.CopyFormView.as_view(), name="forms_copy"),
    path(
        "<int:pk>/submissions/",
        views.SubmissionListView.as_view(),
        name="forms_submissions",
    ),
    path(
        "<int:pk>/submissions/delete/",
        views.SubmissionDeleteView.as_view(),
        name="forms_delete_submissions",
    ),
]


if SettingsModel:  # pragma: no cover
    urlpatterns += [
        path(
            "<int:pk>/advanced/",
            views.AdvancedSettingsView.as_view(),
            name="forms_advanced",
        )
    ]
