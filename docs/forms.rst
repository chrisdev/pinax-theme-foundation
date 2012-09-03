Forms
-----

This theme ships with a basic template tag for rendering forms that match
the markup expected by foundation.

To style forms, add the following to the top of your template ::
    
    {% load foundation_tags %}

and include your form using the following markup: ::
    
    <form method="POST" action="">
        {% csrf_token %}
        <fieldset class="form-controls">
            {{ form|as_foundation }}
        </fieldset>
        <fieldset class="form-actions">
            <button type="submit" class="button medium radius nice"">Submit</button>
        </fieldset>
    </form>

Find more about foundation forms `here`_ .

.. _here: http://foundation.zurb.com/docs/forms.php