try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-dev-urls',
    version='2020.6.4',
    packages=[
        'django_dev_urls',
    ],
)