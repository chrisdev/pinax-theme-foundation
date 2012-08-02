==================================
A Zurb Foundation Theme for Pinax
==================================

Pinax 0.9 based on `Foundation 3`_.  `Zurb Foundation`_
is a popular CSS framework that is light weight, but includes all the basics 
such as; a twelve column responsive grid, forms,dialog, navigation tabs, buttons, typography and so on. 
`Zurb Foundation`_  is not as feature complete as some other frameworks, but this may be one of its advantages. 
It has been argued that frameworks that provide "everything out of the box" tend to encourage the 
development of "cookie cutter" sites and apps. 
You can read more about the ideas behind 
Foundation  and how to use  it for rapid prototyping 
`here <http://www.alistapart.com/articles/dive-into-responsive-prototyping-with-foundation>`_.  

.. _Zurb Foundation: http://foundation.zurb.com

Contributors
-------------
* `Christopher Clarke <https://github.com/chrisdev>`_
* `Kewsi Aguillera <https://github.com/kaguillera>`_
* `Lendl Smith <https://github.com/ilendl2>`_

What's New
--------------------

* Support for foundation 3.0 



Quickstart
-----------
Create a virtual environment for your project and activate it::

    $ virtualenv mysite-env
    $ source mysite-env/bin/activate
    (mysite-env)$
    
Next install Pinax::

    (mysite-env)$ pip install Pinax
    
Once Pinax is installed use **pinax-admin**  to create a project for your site
::

    (mysite-env)$ pinax-admin setup_project mysite -b basic mysite


The example above will create a starter django project in the mysite folder based on the Pinax **basic** project. Of ccourse you can use any of the Pinax starter Projects.  The **basic** project provides features such as 
basic account management as well as user profiles and notifications. The project also comes with a theme - a collection css, javascript files and default templates based on Twitter Bootstrap. 

To use the **zurb-foundation** theme in the project, include "pinax-theme-foundation" in requirements/project.txt. Edit the **settings.py** file and 
comment out the entry for "pinax_theme_bootstrap" and add "pinax_theme_foundation" in your INSTALLED APPS::
     
    # theme
    #"pinax_theme_bootstrap",
    "pinax_theme_foundation",

Inside your project run::

    (mysite-env)$ python manage.py syncdb
    (mysite-env)$ python manage.py runserver

Change the Site name by editing *fixture/initial_data.json*  you can also use the Admin app for this purpose. 

Your "site_base.html" should extend "theme_base.html" and should provide "footer" and "nav" blocks (the latter should just be a ul of li of a links).

Your pages should have blocks "head_title" and "body" and should extend "site_base.html".

The **url** name "home" should be defined as the homepage.

On desktop devices the default viewport width is set to 1200px you may prefer something different. 
To set for example, a 980px wide viewport on desktop devices simply add the following to 
your project style sheet *static/site_sytles.css* ::

	row {
	  max-width: 980px; 
	}

	
.. end-here

Documentation
--------------

See the `full documentation`_ for more details.

.. _full documentation: http://pinax-theme-foundation.readthedocs.org/
.. _Pinax: http://pinaxproject.com
