Settings
========

Any settings with their defaults are listed below for quick reference.

.. code-block:: python

    # the label of the forms area in the admin sidebar
    WAGTAILFORMS_ADMIN_MENU_LABEL = 'Forms'

    # the order of the forms area in the admin sidebar
    WAGTAILFORMS_ADMIN_MENU_ORDER = None

    # the model defined to save advanced form settings
    # in the format of 'app_label.model_class'.
    # Model must inherit from 'wagtailforms.models.AbstractFormSetting'.
    WAGTAILFORMS_ADVANCED_SETTINGS_MODEL = None

    # enable the built in hook to process form submissions
    WAGTAILFORMS_ENABLE_FORM_PROCESSING = True

    # enable the built in hooks defined in wagtailforms
    # currently (save_form_submission_data)
    WAGTAILFORMS_ENABLE_BUILTIN_HOOKS = True

    # the default form template choices
    WAGTAILFORMS_FORM_TEMPLATES = (
        ('forms/form_block.html', 'Default Form Template'),
    )

    # show the form reference field in the list view and export
    WAGTAILFORMS_SHOW_FORM_REFERENCE = True
