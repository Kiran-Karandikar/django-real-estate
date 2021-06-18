# django-real-estate
This repo is for Udemy course "python-django-dev-to-deployment". 

## Steps to install
1. Create Virtual Env
    1. Venv is already packaged in this code but if you want to start from scratch follow step 1 and 2
    2. Venv creation 
        ```
       python -m venv ./venv
       ```
2. Package Installation
> #### Upgrade pip first
````
pip install --upgrade pip
````
> #### Django
````
pip install django;
````
> #### Postgres
````
pip install postgres;
pip install psycopg2;
pip install psycopg2-binary;
````
> #### Media Files support
```
pip install pillow
```
## Database settings
1. Create the required database in postgres
2. Get the connection details like hostname, port, username, password.
3. Check in pgadmin4 for database.
```postgresql
create database btree_db;
\l;
```
### Make server running
1. Change database settings in following file
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
2. Stop the server and make sure the database connection is working.
3. Migrate the sql migrations
```
python manage.py showmigrations;
python manage.py migrate;
```
> Here migrations should run successfully and you should be able to see the status ok
> Otherwise, go back to database and settings.py file and check for any erros.

3. Create admin user
```
python manage.py createsuperuser;
```
3. Static files Collection
````
python manage.py collectstatic
````
##TODO
```
pip install pylint-django
```
```
pip install wheel
```
https://django-extensions.readthedocs.io/en/latest/

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
