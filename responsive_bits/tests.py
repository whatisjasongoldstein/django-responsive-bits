from django.conf import settings
from django.template import Template, Context

settings.configure()
settings.INSTALLED_APPS = ('responsive_bits',)


def test_image_sizes():
    """ Test the template tag. """
    template = Template("""{% load responsive_tags %}<img data-src-sizes={% image_sizes 0="red.jpg" 300="blue.jpg" %}>""")
    html = template.render(Context())
    assert html == u'<img data-src-sizes=\'{"300": "blue.jpg", "0": "red.jpg"}\'>'

