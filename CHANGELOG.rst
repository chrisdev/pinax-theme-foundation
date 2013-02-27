==========
CHANGELOG
==========
0.2.3 (2013/02/26)
------------------
Changes are mainly from our new
contributor `Justin Hamade <https://github.com/justhamade>`_

- Updated all the foundation css classes and included support for the new icon fonts
  To create an icon apply the appropriate classes that match the icon you want to use.
  ::

    <i class="foundicon-[icon]"></i>

- Added demos from the ZURB playground,
  these make a nice visual test to make sure things were working:

    - `Responsive Tables <http://www.zurb.com/playground/responsive-tables>`_
    - `Off canvas layouts <http://www.zurb.com/playground/off-canvas-layouts>`_
    - `Icon Fonts 2 <http://www.zurb.com/playground/foundation-icons>`_

- Added all of the templates from http://foundation.zurb.com/templates.php
- Removed minimized ccs/js in favour of using an inline compressor like django-pipeline.
  This is has currently been implemented in `Account Template <https://github.com/chrisdev/foundation-project-account/>`_
- Fixes for the orbit slider

0.2a2 (2012/11/02)
------------------
- Provide support for the  `--template` for ``django-admin.py startproject``
- Removed ``Pinax`` dependency. Note it will still work with other
  pinax style apps such as django-user-account

0.1.7 (2012/10/18)
------------------

- This release supports Foundation 3.1 which includes features such as
  right-to-left language support, new UI Styles for Progress Bars
  and Image Thumbs, updated jQuery and so on, read more Foundation 3.1
  `here <http://foundation.zurb.com/docs/support.php>`_
- Replaced any of the remnants of our home grown Top Navigation menu
  with the Foundation 3.1 responsive Top Navigation bar
- Included Icon Fonts, Responsive Tables and SVG Social Icons
  which are not part of core release
- Lay the groundwork for supporting the `--template`
  flag on the `django-admin.py start project` in the next release
- Other Bug fixes.

0.1.6 (2012/08/02)
-------------------

- We now support Foundation 3 so you can use features like new
  the new Top Foundation Nav bar
- Support for
  `responsive tables <http://www.zurb.com/playground/responsive-tables>`_
- Simplified the `demo site <http://foundation.chrisdev.com>`_
  so that its just the pinax basic site
- Removed support for responsive design patterns as these were
  not compatible with Foundation 3 release
- Updated documentation to reflect Foundation 3
- Numerous bug fixes.


0.1.5 (2012/06/08)
------------------

- Improved top Navbar based on which is based on foundation's `top-bar
  branch <https://github.com/zurb/foundation/tree/top-bar>`_ .
- Inclusion of `zurb symbol icon
  fonts <https://github.com/zurb/foundation-icons>`_.
- Inclusion of CSS to support the `Responsive Design Patterns`_
  originally discussed by `Joshnua Johson`_ and implemented
  by `Matt Reimer`_
- Updated documentation and set up a `demo site <http://foundation.chrisdev.com>`_
  based on a Pinax basic
  project
- Some reorganization of the *theme\_base.html* including:

   -  Moved (where possible) the javascript to the bottom of the file
   -  Use the `static template
      tag <https://docs.djangoproject.com/en/dev/howto/static-files/#with-a-template-tag>`_
   -  Using the static assets for released version of `zurb-foundation
      2.2.1 <http://foundation.zurb.com/files/foundation-download-2.2.1.zip>`_

-  Fixed numerous bugs


.. _Responsive Design Patterns: http://designshack.net/articles/css/5-really-useful-responsive-web-design-patterns/
.. _Joshnua Johson: http://designshack.net/author/joshuajohnson/
.. _Matt Reimer: http://www.raisedeyebrow.com/bm/blog/2012/04/responsive-design-patterns/

0.1.4 (2012/03/004)
-------------------

-  Added the Fixed top Menubar
-  Show active links on the menubar (Issue #14)
-  Fixed the repositioning of form when timezone is changed on timezone
   page
-  Removed unnecessary cancel button on the modal Profile form
-  Updated the Foundation theme to Zurb Foundation 2.2.0

0.1.3b (2012/2/13)
------------------

-  Added Mobile Login/Sign in functionality

0.1.3
-----

-  Initial release of pinax-theme-foundation
