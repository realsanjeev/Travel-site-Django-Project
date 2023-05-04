# Django

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
$ $ python manage.py makemigration
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
