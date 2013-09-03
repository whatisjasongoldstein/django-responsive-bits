from distutils.core import setup
from setuptools import find_packages

setup(
    name='Django Responsive Bits',
    version="0.1",
    author='Jason Goldstein',
    author_email='jason@betheshoe.com',
    url='https://github.com/whatisjasongoldstein/django-responsive-bits',
    packages=find_packages(),
    include_package_data=True,
    description='Useful bits for building responsive sites in Django.',
    long_description=open('README.md').read(),
)