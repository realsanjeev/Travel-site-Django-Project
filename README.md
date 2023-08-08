# Django Project - Travel-site

```
$ pip install django

$ django-admin startproject <mysite>
```
Add app to site
```
$ python manage.py startapp firstapp

```
### Migrate the model and create superuser
```
$ python manage.py makemigrations
$ python manage.py migrate 
$ python manage.py createsuperuser
```

For codespace. Goto setting.py ad add 
```
if 'CODESPACE_NAME' in os.environ:
    codespace_name = os.getenv("CODESPACE_NAME")
    codespace_domain = os.getenv("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")
    CSRF_TRUSTED_ORIGINS = [f'https://{codespace_name}-8000.{codespace_domain}']
```

curl -H 'Accept: application/json; indent=4' -u admin1:password http://127.0.0.1:8000/users/

### To add Statc directory
```
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]
```
### To extend the layout page in another html page
In another page which extend the content of `layout.html`, we need
```html
{% extends "layout.html" %}
{% block startblock %}
{% endblock starblock %}
```

## Making database migration 
After creating database in models.py
and register model in `<app>/admin.py`
```python
from django.contrib import admin
from <app_name>.models import Contact
# Register your models here.
admin.site.register(Contact)
```

## Log in Form 
settings.py    `AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
`