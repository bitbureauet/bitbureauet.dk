from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def is_active(context, url_name):
    resolved_url = reverse(url_name)
    current_path = context['request'].path
    if resolved_url == current_path:
        return 'active'
    return
