from django import template

register = template.Library()


@register.filter
def instanceof(obj, class_name):
    return obj.__class__.__name__ == class_name
