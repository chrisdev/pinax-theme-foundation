===============================
Zurb Foundation Theme for Pinax
===============================
A theme for Pinax 0.9 based on Zurb Foundation. Zurb Foundation is a popular CSS framework that is built on a 
responsive grid that accommodates devices with a variety of screen sizes.
Documentation on Foundation can be found at http://foundation.zurb.com/docs/

Authors
-------
* Christopher Clarke https://github.com/chrisdev
* Kewsi Aguillera https://github.com/kaguillera

In This Version
--------------------
We've added a number of major feature requests & bug fixes for this release including:
 * The use Zurb Foundation 2.2.0 which will be the last major release in the 2+ series
 * The top navigation bar is now responsive and can support things like drop down lists. 
 * Modals dialogs now now work with forms where the link and the from are on different pages.

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

Foundation is 100% responsive so that you may want to add the following to the project style sheet *static/site_sytles.css*
to handle larger displays::

	row {
	  max-width: 980px; 
	}


Forms
-----

This theme ships with a basic template tag for rendering forms that match
the markup expected by foundation

To style forms, add the following to the top of your template ::
    
    {% load foundation_tags %}

and include your form using the following markup: ::
    
    <form method="POST" action="">
        {% csrf_token %}
        <fieldset class="form-controls">
            {{ form|as_foundation }}
        </fieldset>
        <fieldset class="form-actions">
            <button type="submit" class="button medium radius nice"">Submit</button>
        </fieldset>
    </form>