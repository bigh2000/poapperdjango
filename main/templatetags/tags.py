from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe, SafeData
from django.utils.text import normalize_newlines
from django.utils.html import escape

register = Library()

@stringfilter
def keep_spacing(value, autoescape=None):
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(value)
    if autoescape:
        value = escape(value)
    value = mark_safe(value.replace('  ', ' &nbsp; &nbsp;'))
    value = mark_safe(value.replace('\t', ' &nbsp; &nbsp; &nbsp; &nbsp;'))
    return mark_safe(value.replace('\n', '<br/>'))
register.filter(keep_spacing)