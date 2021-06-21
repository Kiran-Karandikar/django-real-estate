# Django | Real Estate Project
This repo is for Udemy course 
["python-django-dev-to-deployment"](https://www.udemy.com/course/python-django-dev-to-deployment/).

Environment setup
---
> Virtual Environment
```
python -m venv ./venv
```
> Pip and setuptools Upgrade
````
pip install --upgrade pip;
pip install --upgrade setuptools;
pip install wheel;
````
> Django Installation
````
pip install django;
````
> Postgres
````
pip install postgres;
pip install psycopg2;
pip install psycopg2-binary;
````
> Media Files support
```
pip install pillow;
```
> Pylint
```
pip install pylint-django;
```
> Install [Microsoft Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
## Database settings
1. Create the required database in postgres
2. Get the connection details like hostname, port, username, password.
3. Check in pgadmin4 for database.
```postgresql
create database btree_db;
\l;
```
### Server side settings
- Change database settings in following file
````
myproject\settings.py
````
```python

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": "btree_db",
        "USER": "postgres",
        "PASSWORD": "<your_password>",
        "HOST": "localhost",
    }
}
```
- Restart server and make sure the database connection is working.
- Migrate the sql migrations
```
python manage.py showmigrations;
python manage.py migrate;
```
> Here migrations should run successfully and you should be able to see the status ok
> Otherwise, go back to database and settings.py file and check for any erros.

### Admin stuff

- Create admin user
```
python manage.py createsuperuser;
```
- Static files Collection
````
python manage.py collectstatic;
````

### Extras

[django-extensions](https://django-extensions.readthedocs.io/en/latest/)

```
pip install django-extensions
```
You need to add it to installed_apps in your project’s ``settings.py`` file:
```python
INSTALLED_APPS = (
    'django_extensions',
)

```
Generate a graphviz graph of app models

```python manage.py graph_models -a -o myapp_models.png```
Check templates for rendering errors

````pythonpython manage.py validate_templates````
Produce a tab-separated list of tuples for a project

```python manage.py show_urls```
#####Django-filter
```
pip install django-filter
```
Add django_filters in ``INSTALLED_APPS``:
```python
INSTALLED_APPS = [
    'django_filters',
]

```
```
pip install django-import-export
```
Change INSTALLED_APPS of ``setting.py``:
```python
INSTALLED_APPS = (
    'import_export',
)
```
