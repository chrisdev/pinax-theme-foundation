======================================
A Foundation Theme for Django Projects
======================================

A Pinax theme + based on `Zurb Foundation`_
Foundation is a popular CSS framework that is light weight, but includes
all the basics such as; a responsive grid, forms, dialog, navigation tabs,
buttons, typography and so on.
You can read more about the ideas behind
Foundation  and how to use  it for rapid prototyping in this `article`_.

.. _Zurb Foundation: http://foundation.zurb.com
.. _article: http://www.alistapart.com/articles/dive-into-responsive-prototyping-with-foundation/

Contributors
-------------
* `Christopher Clarke <https://github.com/chrisdev>`_
* `Kewsi Aguillera <https://github.com/kaguillera>`_
* `Lendl R Smith <https://github.com/ilendl2>`_


What's New
------------

- Supports the  `--template` for ``django-admin.py startproject``
- Removed explicit ``Pinax`` dependency. Although it will still work with other
  pinax style apps such as django-user-account


Quickstart
-----------
To Use ::
    mkvirtualenv mysite
    pip install Django==1.4.1
    django-admin.py startproject --template=https://github.com/pinax/pinax-project-account/zipball/master mysite
    cd mysite
    pip install -r requirements.txt
    python manage.py syncdb && python manage.py runserver


Templates
^^^^^^^^^^

You should provide your own "footer" template _footer.html

Also change the Site name by editing *fixture/initial_data.json*  you can also use the Admin app for this purpose.
The **url** name "home" should be defined as the homepage.


Upgrading Previous Version
---------------------------
To upgrade you site start by upgrading to the latest version on pinax-theme-foundation ::

    pip install -- upgrade pinax-theme-foundation

The big change between Foundation 2 to 3 is the grid. In Foundation 3 you no longer have to use *.container*
to define the grid. In Foundation 2 the grid was built around
*.container > .row > .columns* in Foundation 3 you now just have to use *.row > .columns*.
In Foundation 3 padding and borders no longer increase the width of an element,
they only go inward so for example in Foundation 3 .three.columns always has a width of 25%
with a 15px padding on the left and right.
You can find the Foundation 3 migration guide `here <http://foundation.zurb.com/migration.php>`_
Remove all **max-width** from css sytling




.. end-here

Documentation
--------------

See the `full documentation`_ for more details.

.. _full documentation: http://pinax-theme-foundation.readthedocs.org/
.. _Pinax: http://pinaxproject.com
