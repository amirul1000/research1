from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


@register.filter(name="color_text")
@stringfilter
def color_text(value, arg):
    new = '<span style="background-color: #b2ebf2; padding: 5px; margin-bottom: 10px; border: 1px solid #a7a7a7; display: inline-block; border-radius: 10px;">'+arg+'</span>'
    pattern = re.compile(arg,re.IGNORECASE)
    str_data = pattern.sub(arg, value)
    if len(arg.strip())>0:
    	return str_data.replace(arg,new)
    return value