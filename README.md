<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-dev-urls.svg?maxAge=3600)](https://pypi.org/project/django-dev-urls/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-dev-urls.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-dev-urls.py/actions)

### Installation
```bash
$ [sudo] pip install django-dev-urls
```

#### Examples
`urls.py`
```python
from django_dev_urls.urls import urlpatterns

urlpatterns += [
    ...
]
```

equivalent of
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
