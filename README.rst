clear
Wagtail Forms
===================

|tests| |Codecov| |pypi| |github|

Allows you to build forms in the CMS admin area and add them to any StreamField in your site.
You can add your own fields along with the vast array of default fields which include the likes
of file fields. Form submissions are controlled by hooks that you can add that process the forms cleaned data.
Templates can be created which will then appear as choices when you build your form,
allowing you to display and submit a form however you want.



What else is included?
----------------------

*  Each form is built using a StreamField.
*  Customise things like success and error messages, post submit redirects and more.
*  Forms are processed via a ``before_page_serve`` hook. Meaning there is no fuss like remembering to include a page mixin.
*  The hook can easily be disabled to provide the ability to create your own.
*  Form submissions are controlled via hooks meaning you can easily create things like emailing the submission which you can turn on and off on each form.
*  Fields can easily be added to the form from your own code such as Recaptcha or a Regex Field.
*  The default set of fields can easily be replaced to add things like widget attributes.
*  You can define a model that will allow you to save additional settings for each form.
*  Form submissions are also listed by their form which you can filter by date and are ordered by newest first.
*  Files can also be submitted to the forms that are shown with the form submissions.
*  A form and its fields can easily be copied to a new form.
*  There is a template tag that can be used to render a form, in case you want it to appear outside a StreamField.

Documentation
-------------

Can be found on `readthedocs <http://wagtailforms.readthedocs.io/>`_.

Screenshots
-----------

.. figure:: http://wagtailforms.readthedocs.io/en/latest/_images/screen_1.png
   :width: 728 px

   Example Front End

.. figure:: http://wagtailforms.readthedocs.io/en/latest/_images/screen_3.png
   :width: 728 px

   Form Fields Selection

Example site with docker
------------------------

Clone the repo

.. code:: bash

    $ git clone https://github.com/lumunix/wagtailforms.git

Run the docker container

.. code:: bash

    $ cd wagtailforms
    $ docker-compose up

Create yourself a superuser

.. code:: bash

    $ docker-compose exec app bash
    $ python manage.py createsuperuser

Go to http://127.0.0.1:8000

.. |tests| image:: https://github.com/lumunix/wagtailforms/workflows/Python%20Tests/badge.svg
   :target: https://github.com/lumunix/wagtailforms/actions?query=workflow%3A%22Python+Tests%22
.. |Codecov| image:: https://codecov.io/gh/lumunix/wagtailforms/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lumunix/wagtailforms
.. |pypi| image:: https://img.shields.io/pypi/v/wagtailforms.svg
   :target: https://pypi.org/project/wagtailforms/
.. |github| image:: https://img.shields.io/github/stars/lumunix/wagtailforms.svg?style=social&logo=github
   :target: https://github.com/lumunix/wagtailforms/stargazers

