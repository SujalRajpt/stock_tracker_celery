from django import template

register = template.Library()


@register.filter
def billions(value):
    try:
        value = float(value)
        return f"{value / 1_000_000_000:.2f}B"
    except (TypeError, ValueError):
        return "N/A"


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
