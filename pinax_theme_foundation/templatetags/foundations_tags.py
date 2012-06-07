from django.template import Context
from django.template.loader import get_template
from django import template


register = template.Library()


@register.filter
def as_foundation(form):
    template = get_template("foundation/form.html")
    c = Context({"form": form})
    return template.render(c)
