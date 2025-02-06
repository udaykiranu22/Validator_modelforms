from django import template

register = template.Library()

# normal method to register
def swap(value):
    return value.swapcase()

# decorator method, if you don't want to change function name
@register.filter()
def capitalize(value):
    return value.capitalize()

# decorator method, if you want to change function name

@register.filter()
def counters(value,arg):
    return value.count(arg)

register.filter('swapping', swap)