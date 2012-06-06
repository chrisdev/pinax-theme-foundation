Top Navbar
----------

The current release of foundation, `version
2.2.1 <http://foundation.zurb.com/files/foundation-download-2.2.1.zip>`_
does not provide a *Top Navbar* component similar to the one provided by
`twitter bootstrap <http://twitter.github.com/bootstrap/>`_. As this is
a requirement for many projects, we have included a *Top Navbar*
component which is loosely based on `foundation top-bar
branch <https://github.com/zurb/foundation/tree/top-bar>`_ .

To use the *Top Navbar* in your your project, first ensure that your
project's *site\_base.html* inherits from *theme\_base.html*

::

    {% extends "theme_base.html" %}

*theme\_base.html* defines the template block *topbar* with the
following structure.

::

            {% block topbar %} 
                <div class="attached">
                    <div class="name">
                        <span><a href="/">{{SITE_NAME}}</a><a href="#" class="toggle-nav"></a></span>
                    </div>  
                    <ul class="right">
                        {% block account_bar %}{% include "_account_bar.html" %}{% endblock %}
                    </ul>
                    {% block nav %} {% endblock %}
                </div>
            {% endblock %}

This will provide your project with a *navbar* which is fixed to the top
of the site (via the "attached" class) which displays the *SITE\_NAME*
and an account management drop down menu. The account management drop
down is simply an unordered lists as shown in the following snippet
abstracted from the *\_account\_bar.html* template file

::

    {% if user.is_authenticated %}
        <li class="has-dropdown">
            <a href="#">{{ user }}</a>
            <ul class="dropdown">
                <li><a href="{% url acct_email %}"><span class="glyph social">x</span>Account</a></i></li>
                {% if user.is_staff %}
                        <li><a href="{% url admin:index %}"><span class="glyph general">a</span>Admin</a></li>
                {% endif %}
                <li><a href="{% url acct_logout %}"><span class="glyph general">]</span>Log&nbsp;out</a></li>
            </ul>
        </li>
        &hellip;

So to create a drop down menu item, simply assign the *li* element the
*"has-dropdown"* class and include an unordered list element with a
"dropdown" class selector ``<ul class="dropdown">`` that contains the
drop down menu items . The *nav* block can be utilized for the other
menu items for the site. These can be a combination of drop down and non
drop down elements. This is shown in the following snippet abstracted
from the *Top Navbar* for this site

::

    <li><a href="/">Home</a></li>
        {% if user.is_authenticated %}
    <li id="tab_profile"><a href="{% url profile_detail user.username %}">{% trans "Profile" %}</a></li>
    <li id="tab_notices"><a href="{% url notification_notices %}">{% trans "Notices" %}{% if notice_unseen_count %} ({{ notice_unseen_count }}){% endif %}</a></li>
        {% endif %}
    <li class="has-dropdown">
            <a href="http://apps.raisedeyebrow.com/Design_Patterns/" target="_blank">Design Patterns</a>
            <ul class="dropdown">
                <li><a href="/mondrian/"><span class="glyph general">d</span>Mondrian</a></li>
                <li><a href="/column_flip/"><span class="glyph general">c</span>Column Flip</a></li>
                <li><a href="/gallery_design/"><span class="glyph general">a</span>Gallery Design</a></li>
                <li><a href="/featured_items/"><span class="glyph general">i</span>Featured Items</a></li>
                <li><a href="/foundation_grid/"><span class="glyph general">p</span>Foundation Grid</a></li>
                <li><a href="/featured_shuffle/"><span class="glyph general">b</span>Featured Shuffle</a></li>
            </ul>
    </li> 

It should be noted that menu items can be embellished with appropriate
symbol icons by including a span element with the *"glyph general"*
class selector. So adding

::

     <span class="glyph general">a</span>

will display the "gear" icon. These are actually `Zurb symbol icon
font <https://github.com/zurb/foundation-icons>`_ that will scale and
display nicely on various devices. These can be used any where in your
project. .
