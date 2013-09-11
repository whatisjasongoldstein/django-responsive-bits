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

    <img data-src-sizes={% image_sizes 0=small_image_easythumb.url 300=medium_image_easythumb.url %}>
    """
    for k, v in kwargs.items():
        kwargs[k] = v
    
    return "'{}'".format(json.dumps(kwargs))


@register.simple_tag
def image_sizes_css(selector="", default="", **kwargs):
    """
    Pass a selector, a default size, and kwargs as min-img-width=url

    <figure id="#foobar"></figure>
    {% image_sizes_css selector="#foobar" default=default_image 1024=medium_image 1680=large_image %}

    """
    default = "{} {{ background-image: url('{}'); }}".format(selector, default)
    rules = [default, ]
    for k, v in kwargs.items():
        rule = """
        @media (min-width: {width}px){{
            {selector} {{ background-image: url('{url}') }};
        }}
        """.format(selector=selector, width=k, url=v)
        rules.append(rule)
    rules = "\n".join([r for r in rules])
    html = """<style type="text/css">{}</style>""".format(rules)
    return html