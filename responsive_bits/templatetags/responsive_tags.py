try:
    import json
except ImportError:
    import simplejson as json

from django import template
register = template.Library()

@register.simple_tag
def image_sizes(**kwargs):
    """
    Pass kwargs as min-img-width=url

    Don't wrap it in quotes.

    <img data-src-sizes={% image_sizes 0=small_image_easythumb 300=medium_image_easythumb %}>
    """
    for k, v in kwargs.items():
        kwargs[k] = v.url
    
    return "'{}'".format(json.dumps(kwargs))