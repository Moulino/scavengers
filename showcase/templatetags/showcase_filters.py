from django import template
import logging

logger = logging.getLogger(__name__)

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError) as e:
        logger.error(f"Error in multiply filter: {e}")
        return ''

@register.filter(name='divide')
def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError, ZeroDivisionError) as e:
        logger.error(f"Error in divide filter: {e}")
        return '' 