from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="assets_static")
@stringfilter
def assets_static(value, arg):
    return value.replace(arg,"static")