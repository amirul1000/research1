from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="replace")
@stringfilter
def replace(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, ' ')
