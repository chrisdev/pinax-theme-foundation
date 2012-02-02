from setuptools import setup, find_packages

LONG_DESCRIPTION = """
===============================
Zurb Foundation Theme for Pinax
===============================
A theme for Pinax 0.9 based on Zurb Foundation. Zurb Foundation is a popular CSS framework that is built on a 
responsive grid that accommodates devices with a variety of screen sizes.
Documentation on Foundation can be found at [here](http://foundation.zurb.com/docs/)

Authors
--------

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
* build additional templates for other Pinax-related apps
* Find a proper solution to the top navigation bar. The Foundation framework does not currently contain a top navigation bar we are currently
  using the "zurBar" foun on the document site. This bar does no support drop down items
* Add responive tags to starter templates to fully support mobile devices
* Add templates for all the standard Pinax   apps.


"""
PACKAGE = "pinax_theme_foundation"
NAME = "pinax-theme-foundation"
DESCRIPTION = "Pinax theme based on Zurb's Foundation"
AUTHOR = "Chris Clarke"
AUTHOR_EMAIL = "cclarke@chrisdev.com"
URL = "http://github.com/chrisdev/pinax-theme-foundation"
VERSION = __import__(PACKAGE).__version__


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests","example_project"]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False,
)
