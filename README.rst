==================================
A Foundation 3 Theme for Pinax
==================================

Pinax 0.9 + based on `Zurb Foundation`_
is a popular CSS framework that is light weight, but includes all the basics 
such as; a twelve column responsive grid, forms,dialog, navigation tabs, buttons, typography and so on. 
`Zurb Foundation`_  is not as feature complete as some other frameworks, but this may be one of its advantages. 
It has been argued that frameworks that provide "everything out of the box" tend to encourage the 
development of "cookie cutter" sites and apps. 
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
--------------------

- We now support Foundation 3. This means that you can now all the neat  Foundation 3's  features such as the new Nav bar.
- Support for responsive tables
- Removed support for responsive design patterns as its not compatible with Foundation 3
- Simplified the `demo site <http://foundation.chrisdev.com>`_
- Updated documentation to reflect the use of Foundation 3
- Numerous bug fixes.

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

The example above will create a starter Django project in the mysite folder based on the Pinax **basic** project.
Of course you can use any of the Pinax starter Projects.  
The **basic** project provides features such as account management, user profiles and notifications. 
The starter project also comes with a **theme** or a collection css, javascript files.  
The default theme is based on Twitter Bootstrap. 

To use the **Foundation** theme in the project, include "pinax-theme-foundation" in requirements/project.txt. 
Either install the package individually. ::
    
    pip install pinax-theme-foundation
    
Or use the requirements file::

    pip install -r requirements/project.txt
    
   
Next edit the **settings.py** file and 
comment out the entry for "pinax_theme_bootstrap" and add "pinax_theme_foundation" in your INSTALLED APPS::
     
    # theme
    #"pinax_theme_bootstrap",
    "pinax_theme_foundation",

Inside your project run::

    (mysite-env)$ python manage.py syncdb
    (mysite-env)$ python manage.py runserver


Templates
^^^^^^^^^^
The Pinax *setup_project* creates a *site_base.html* template which extends *theme_base.html*. 
You own templates should normally inherit from *site_base.html*.  However, due to
inconsistencies between Bootstrap and Foundation you may need to perform an additional step
to ensure that the top nav bar is styled properly.
If have created a **basic** starter project 
edit the generated *site_base.html* to remove the extra
*ul* tags found in the *{% nav block %}*. In the *basic* project  *{% nav block %}* contains profile and notices dropdown menu items.  
The project  *site_base.html*  will contain ::
    
    {% block nav %}
		{% if user.is_authenticated %}
		<ul>{% spaceless %}
			<li id="tab_profile"><a href="{% url profile_detail user.username %}">{% trans "Profile" %}</a></li>
			<li id="tab_notices"><a href="{% url notification_notices %}">{% trans "Notices" %}{% if notice_unseen_count %} ({{ notice_unseen_count }}){% endif %}</a></li>
			{% endspaceless %}
		 </ul>
		{% endif %}
   {% endblock %}

Remove the *ul* tags so the block looks like ::

	 {% block nav %}
		{% if user.is_authenticated %}
			<li id="tab_profile"><a href="{% url profile_detail user.username %}">{% trans "Profile" %}</a></li>
			<li id="tab_notices"><a href="{% url notification_notices %}">{% trans "Notices" %}{% if notice_unseen_count %} ({{ notice_unseen_count }}){% endif %}</a></li>
		{% endif %}
	  % endblock %}



You should provide your own "footer" template _footer.html

Also change the Site name by editing *fixture/initial_data.json*  you can also use the Admin app for this purpose. 
The **url** name "home" should be defined as the homepage.


Upgrading Previous Version
---------------------------------------------
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
