from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='cut')
@stringfilter
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    :param value: string
    :param arg: string
    :return: string
    """
    return value.replace(arg, '')
