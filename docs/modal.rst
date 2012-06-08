Modal Dialogs
---------------

`Reveal`_ is foundation's modal dialog
The easiest way to use reveal  dialogs with your `pinax_` forms
is to first create a separate template for the form  
as shown in this simplified example taken from  the `idios`_ app. ::

	{% extends "idios/base.html" %}
    {% load foundations_tags %}
	{% load i18n %}
	
	{% block head_title %}{% trans "Edit Profile" %}{% endblock %}
	
	
	{% block body %}
	<form class="nice" method="POST" action="{% url profile_edit %}">
		{% csrf_token %}
		<fieldset>
			{{ profile_form|as_foundation }}
		</fieldset>
		<div class="actions">
			<button type="submit" class="button medium radius nice">Update</button>
		</div>
	</form> 
	{% endblock %}

In the template (*idios/profile.html*) where you to show the modal form,
add the *"reveal"*  class selector and give it an id (*edit-profile-box*)
to the object which you want to fire the modal when clicked::

	<a id="edit-profile-box" href="{% url profile_edit %}" class="button reveal">Edit profile</a>
 
The *href* ``{% url profile_edit %}`` url will display the form.
Finally add the following javascript to the template. 
::

	{% block extra_body %}
	<script>
	   $('#edit-profile-box').click(function(event) {
			event.preventDefault();
			var $div = $('<div>').addClass('reveal-modal').appendTo('body');
			$this = $(this);
			$.get($this.attr('href'), function(data) {
			  return $div.empty().html(data).append('<a class="close-reveal-modal">&#215;</a>').reveal();
			});
	});
	</script>
	{% endblock %}
	
It should be noted that
 
.. _pinax: http://pinaxproject.com
.. _Reveal: http://http://foundation.zurb.com/docs/reveal.php
.. _idios: http://oss.eldarion.com/idios/docs/0.1/
