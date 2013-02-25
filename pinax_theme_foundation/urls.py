from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    # Icon Demos
    url(r"^/demo/icons/general/", direct_to_template, {
        "template": "foundation/icons/general_icons.html",
    }, name="general_icon"),
    url(r"^demo/icons/social/", direct_to_template, {
        "template": "foundation/icons/social_icons.html",
    }, name="social_icons"),
    url(r"^demo/icons/accessibility/", direct_to_template, {
        "template": "foundation/icons/accessibility_icons.html",
    }, name="accessibility_icons"),
    # Template Examples from http://foundation.zurb.com/templates.php
    url(r"^demo/templates/workspace/", direct_to_template, {
        "template": "foundation/templates/workspace_base.html",
    }, name="workspace_template"),
    url(r"^demo/templates/blog/", direct_to_template, {
        "template": "foundation/templates/blog_base.html",
    }, name="blog_template"),
    url(r"^demo/templates/contact/", direct_to_template, {
        "template": "foundation/templates/contact_base.html",
    }, name="contact_template"),
    url(r"^demo/templates/feed/", direct_to_template, {
        "template": "foundation/templates/feed_base.html",
    }, name="feed_template"),
    url(r"^demo/templates/grid/", direct_to_template, {
        "template": "foundation/templates/grid_base.html",
    }, name="grid_template"),
    url(r"^demo/templates/homepage-1/", direct_to_template, {
        "template": "foundation/templates/homepage-1_base.html",
    }, name="homepage-1_template"),
    url(r"^demo/templates/homepage-2/", direct_to_template, {
        "template": "foundation/templates/homepage-2_base.html",
    }, name="homepage-2_template"),
    url(r"^demo/templates/marketing/", direct_to_template, {
        "template": "foundation/templates/marketing_base.html",
    }, name="marketing_template"),
    url(r"^demo/templates/sidebar/", direct_to_template, {
        "template": "foundation/templates/sidebar_base.html",
    }, name="sidebar_template"),
    # Playground examples
    url(r"^demo/playground/responsive-tables/", direct_to_template, {
        "template": "foundation/playground/responsive-tables.html",
    }, name="responsive_tables"),
    url(r"^demo/playground/offcanvas-1/", direct_to_template, {
        "template": "foundation/playground/offcanvas-1.html",
    }, name="offcanvas-1"),
    url(r"^demo/playground/offcanvas-2/", direct_to_template, {
        "template": "foundation/playground/offcanvas-2.html",
    }, name="offcanvas-2"),
    url(r"^demo/playground/offcanvas-3/", direct_to_template, {
        "template": "foundation/playground/offcanvas-3.html",
    }, name="offcanvas-3"),
    url(r"^demo/playground/offcanvas-4/", direct_to_template, {
        "template": "foundation/playground/offcanvas-4.html",
    }, name="offcanvas-4"),
)
