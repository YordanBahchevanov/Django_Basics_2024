from datetime import datetime
from django import template

register = template.Library()


@register.inclusion_tag('common/user-info.html')
def user_info(user):
    if user.is_authenticated:
        return {
            'username': user.username,
        }

    return {
        'username': "Anonymous",
    }
