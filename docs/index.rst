===============================
Zurb Foundation Theme for Pinax
===============================
A theme for Pinax 0.9 based on Zurb Foundation. Zurb Foundation is a popular CSS framework that is built on a 
responsive grid that accommodates devices with a variety of screen sizes.
Documentation on Foundation can be found at http://foundation.zurb.com/docs/

Authors
--------
* `Christopher Clarke: <https://github.com/chrisdev>`_

* `Kewsi Aguillera: <https://github.com/kaguillera>`_

Quickstart
-----------
Include "pinax-theme-foundation" in your requirements file and "pinax_theme_foundation" in your INSTALLED APPS.

Make sure both template loaders and staticfiles finders includes app directories.

Site name comes from Sites fixture.

Your "site_base.html" should extend "theme_base.html" and should provide "footer" and "nav" blocks (the latter should just be a ul of li of a links).

Your pages should have blocks "head_title" and "body" and should extend "site_base.html".

The url name "home" should be defined as the homepage.


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
            <button type="submit" class="btn primary">Submit</button>
        </fieldset>
    </form>
 
Todo / Issues
--------------
* Add more support for mobile devices
* Try to get the foundation modals (reveal) to support Ajax 
