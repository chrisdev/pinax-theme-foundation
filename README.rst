======================================
A Foundation Theme for Django Projects
======================================

A Pinax theme based on `Zurb Foundation`_.
Foundation is a popular CSS framework that is light weight, but includes
all the basics such as; a responsive grid, forms, dialog, navigation tabs,
buttons, typography and so on.
You can read more about the ideas behind
Foundation and how to use  it for rapid prototyping in this `article`_.

.. _Zurb Foundation: http://foundation.zurb.com
.. _article: http://www.alistapart.com/articles/dive-into-responsive-prototyping-with-foundation/

Contributors
-------------
* `Christopher Clarke <https://github.com/chrisdev>`_
* `Lendl R Smith <https://github.com/ilendl2>`_
* `Kewsi Aguillera <https://github.com/kaguillera>`_
* `Justin Hamade <https://github.com/justhamade>`_


What's New
-----------
This version supports Foundation 4 \o/


Getting Started
----------------
Start by creating a new virtualenv for your project and install Django 1.4 ::

    mkvirtualenv mysite
    pip install Django==1.4.5

Next, use the ``startproject`` management command
to create a new Django project
with a layout as specified in starter project (template URL).
We provide you with two Foundation based starter projects

- zero_
- account_

To use create a project based on the zero_ project run ::

    django-admin.py startproject mysite --template=https://github.com/chrisdev/foundation-project-zero/zipball/master

This will create a new Django project in the mysite directory with:

 - An apps folder for your internal apps
 - initial data (for handling ``sites.Site`` model)
 - Requirements files for use with pip_
 - A home for your site's static files
 - A set of templates designed to work with the foundation theme

Finally install the requirements, sync your database and
start the test server ::

    cd mysite
    pip install -r requirements.txt
    python manage.py syncdb && python manage.py runserver

The account_ starter project provides all the features of the zero project in
addition to incorporating features to support `django-user-account`_.

`django-user-account`_ is an extremely useful ``Pinax`` app that
works in conjunction with django.contrib.auth to
take your Django project from having simple log in, log out and password reset
to a full blown account management system. To create a project based on the
account starter project ::

    django-admin.py startproject --template=https://github.com/chrisdev/foundation-project-account/zipball/master mysite


.. _account: https://github.com/chrisdev/foundation-project-account/
.. _zero: https://github.com/chrisdev/foundation-project-zero/
.. _django-user-account: https://github.com/pinax/django-user-accounts/
.. _pip: http://www.pip-installer.org/en/latest/

Templates
^^^^^^^^^^
Your own templates should normally inherit from ``site_base.html``.
You should provide your own "footer" template ``_footer.html``.

Also change the Site name by editing ``fixture/initial_data.json``.
You can also use the Admin app for this purpose.

The **url** name "home" should be defined as the homepage.


Upgrading From Previous Versions
--------------------------------
To upgrade your site start by upgrading to the latest version
on pinax-theme-foundation ::

    pip install -- upgrade pinax-theme-foundation

The big change between Foundation 2 to 3 is the grid.
In Foundation 3 you no longer have to use *.container*
to define the grid. In Foundation 2 the grid was built around
``*.container > .row > .columns*``. In Foundation 3
you now just need to use ``*.row > .columns*``.
In Foundation 3 padding and borders no longer increase
the width of an element,
they only go inward so for example in Foundation 3 ``.three.columns``
always has a width of 25% with a 15px padding on the left and right.
You can find the Foundation 3 migration guide
`here <http://foundation.zurb.com/migration.php>`_

.. end-here

Documentation
--------------

See the `full documentation`_ for more details.

.. _full documentation: http://pinax-theme-foundation.readthedocs.org/
.. _Pinax: http://pinaxproject.com


License & Attribution
---------------------

The Pinax Foundation Theme theme is released under the MIT license.
This project may include templates and other code from the Pinax project

This theme includes styles and scripts from the Zurb Foundation
which is released under the MIT license

For copies of licenses, see LICENSE.
