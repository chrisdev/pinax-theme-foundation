Top Navbar
----------

`Foundation 3 <http://foundation.zurb.com/files/foundation-download-e.zip>`_
now includes a top nav bar includes the main nav options as well as hover dropdowns 
that support either a list of anchors or arbitrary content (even Grid content).

To use the *Top Navbar* in your your project, first ensure that your
project's *site\_base.html* inherits from *theme\_base.html*

::

    {% extends "theme_base.html" %}


*theme\_base.html* defines the template block *topbar* with the
following structure.

::
   
    {% block topbar_base %}
    	<div class="attached">
        	<div class="row"> 	
    			<li class="name mobile-four">
    				<a href="/">{{SITE_NAME}}</a><a href="#"></a>
    			</li>
    			<ul class="nav-bar menu mobile-four">
    				{% block topbar %}
    					{% block nav %}{% endblock %}
    					{% block account_bar %}
    						{% include "_account_bar.html" %}
    					{% endblock %}
    				{% endblock %}
    			</ul>
    		</div>
    	</div>
    {% endblock %}


This will provide your project with a top *nav bar* which is attached to the top of the page
that  displays the *SITE\_NAME*
and an account management drop down menu. The account management drop
down is simply an unordered lists as shown in the following snippet
abstracted from the *\_account\_bar.html* template file

::

    {% if user.is_authenticated %}
        <li class="has-flyout">
            <a href="#">{{ user }}</a>
            <a href="#" class="flyout-toggle"><span> </span></a>
            <ul class="flyout">
                <li><a href="{% url acct_email %}"><span class="glyph social">x</span>Account</a></i></li>
                {% if user.is_staff %}
                        <li><a href="{% url admin:index %}"><span class="glyph general">a</span>Admin</a></li>
                {% endif %}
                <li><a href="{% url acct_logout %}"><span class="glyph general">]</span>Log&nbsp;out</a></li>
            </ul>
        </li>
    {% endif %}

So to create a drop down menu item, simply assign the *li* element the
*"has-flyout"* class and include an unordered list element with a
"flyout" class selector ``<ul class="flyout">`` that contains the
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
   

It should be noted that menu items can be embellished with appropriate
symbol icons by including a span element with the *"glyph general"*
class selector. So adding :

::

     <span class="glyph general">a</span>


will display the "gear" icon. These are actually `Zurb symbol icon
font <https://github.com/zurb/foundation-icons>`_ that will scale and
display nicely on various devices. These can be used any where in your
project.