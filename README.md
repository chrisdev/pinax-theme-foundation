# Pinax Theme Foundation
This is a Pinax theme based on Zurb Foundation is a popular CSS framework that is built on a 
responsive grid that accommodates devices with a variety of screen sizes.
Documentation on Foundation can be found at [here](http://foundation.zurb.com/docs/)


## Usage

* Include "pinax-theme-foundation" in your requirements file and
"pinax_theme_foundation" in your INSTALLED APPS.

* Make sure both template loaders and staticfiles finders includes
app directories.

* Site name comes from Sites fixture.

* Your "site_base.html" should extend "theme_base.html" and should provide
"footer" and "nav" blocks (the latter should just be a ul of li of a links).

* Your pages should have blocks "head_title" and "body" and should extend
"site_base.html".

* The url name "home" should be defined as the homepage.

## Notes

## TODO

1. Fix the Error boxes under the text fields
2. Figure out how to apply nice to the select option input field
3. Make the menu bar thinner.