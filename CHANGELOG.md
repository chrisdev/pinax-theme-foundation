# CHANGELOG for pinax-theme-foundation

## 0.1.5 (2012/05/30)

 * Improved top Navbar based on which is based on foundation's [top-bar branch](https://github.com/zurb/foundation/tree/top-bar) .
 * Inclusion of [zurb symbol icon fonts](https://github.com/zurb/foundation-icons).
 * Inclusion of CSS to support the [Responsive Design Pattern](http://designshack.net/articles/css/5-really-useful-responsive-web-design-patterns/) originally discussed by [Joshnua Johson](http://designshack.net/author/joshuajohnson/)  and 
implement by [Matt Reimer](http://www.raisedeyebrow.com/bm/blog/2012/04/responsive-design-patterns).
* Updated documentation set up a [demo site](http://foundation.chrisdev.com) based on a pinax basic project
 * Some reorganization of the *theme_base.html* including:
	 * Moved (where possible) the javascript to the bottom of the file 
	*  Use the [static template tag](https://docs.djangoproject.com/en/dev/howto/static-files/#with-a-template-tag) 
	*  Using the static assets for released version of [zurb-foundation 2.2.1](http://foundation.zurb.com/files/foundation-download-2.2.1.zip)
	 
 * Fixed numerous bugs
 
## 0.1.4 (2012/03/004)

 * Added the Fixed top Menubar 
 * Show active links on the menubar (Issue #14)
 * Fixed the repositioning of form when timezone is changed on timezone page 
 * Removed unnecessary cancel button on the modal Profile form
 * Updated the Foundation theme to Zurb Foundation 2.2.0

## 0.1.3b (2012/2/13)

 * Added Mobile Login/Sign in functionality

## 0.1.3

 * Initial release of pinax-theme-foundation
