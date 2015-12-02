import json
import lxml.html
import urlparse
from django import template
from django.utils.safestring import mark_safe

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
    
    return mark_safe("'{}'".format(json.dumps(kwargs)))


@register.filter
def wrap_videos(html):

    # Skip unnecessary postprocessing
    if not "iframe" in html:
        return html

    # Skip unparseable html
    try:
        fragment = lxml.html.fromstring(html)
    except Exception as e:
        return html

    # Wrap all iframes with their slugified domain
    for iframe in fragment.cssselect("iframe"):
        
        # Fix a dumb lxml bug that decides iframes should be
        # self-closing, which isn't valid in html5.
        if not iframe.text:
            iframe.text = " "

        src = iframe.attrib.get("src", "")
        domain_cls = urlparse.urlparse(src).netloc.replace(".","-")

        wrapper = lxml.etree.Element("div")
        wrapper.attrib['class'] = "embed-wrapper %s" % domain_cls

        iframe.addnext(wrapper)
        wrapper.insert(0, iframe)

    return mark_safe(lxml.etree.tounicode(fragment))
    return lxml.etree.tounicode(fragment)

