<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[contributors-shield]: https://img.shields.io/github/contributors/kiran-karandikar/django-real-estate?style=for-the-badge
[contributors-url]: https://github.com/Kiran-Karandikar/django-real-estate/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Kiran-Karandikar/django-real-estate?style=for-the-badge
[forks-url]: https://github.com/Kiran-Karandikar/django-real-estate/network
[stars-shield]: https://img.shields.io/github/stars/Kiran-Karandikar/django-real-estate?style=for-the-badge
[stars-url]: https://github.com/Kiran-Karandikar/django-real-estate/stargazers
[issues-shield]: https://img.shields.io/github/issues/Kiran-Karandikar/django-real-estate?style=for-the-badge
[issues-url]: https://github.com/Kiran-Karandikar/django-real-estate/issues
[license-shield]: https://img.shields.io/github/license/Kiran-Karandikar/django-real-estate?style=for-the-badge
[license-url]: https://github.com/Kiran-Karandikar/django-real-estate/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kiran-karandikar

---

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">django-real-estate</h3>
  <p align="center">
    This repo is for Udemy course "python-django-dev-to-deployment".     
    <br />    
    <a href="https://kiran-karandikar.github.io/django-real-estate"><strong>Preview</strong></a>
    <br />
    <a href="https://github.com/kiran-karandikar/django-real-estate"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kiran-karandikar/django-real-estate">View Demo</a>
    ·
    <a href="https://github.com/kiran-karandikar/django-real-estate/issues">Report Bug</a>
    ·
    <a href="https://github.com/kiran-karandikar/django-real-estate/issues">Request Feature</a>
  </p>
</div>

<!-- BADGES.MD Finish -->
<!-- BADGES.MD Finish -->
# Django | Real Estate Project
- This repo is for Udemy course 
["python-django-dev-to-deployment"](https://www.udemy.com/course/python-django-dev-to-deployment/).
- [Django Deployment](https://gist.github.com/bradtraversy/cfa565b879ff1458dba08f423cb01d71) Guide

## Environment
#### Installation using pipenv
```
pip install pipenv;
pipenv install;
```
#### Standard Installation
> Virtual Environment
```
python -m venv ./venv
```
> Pip and setuptools etc.
````
pip install --upgrade pip;
pip install --upgrade setuptools;
pip install wheel;
pip install autopep8;
````
> Pylint
```
pip install pylint-django;
```
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
> List of django extensions
>> For every extension You need to add it to installed_apps in your project’s ``settings.py`` file

- #### [django-extensions](https://django-extensions.readthedocs.io/en/latest/)

```
pip install django-extensions;
```
```python
INSTALLED_APPS = (
    'django_extensions',
)
```
##### Generate a graphviz graph of app models

```
python manage.py graph_models -a -o myapp_models.png;
```

##### Check templates for rendering errors

```
python manage.py validate_templates;
```
##### Produce a tab-separated list of tuples for a project

```
python manage.py show_urls;
```
- #### [Django-filter](https://django-filter.readthedocs.io/en/stable/index.html)
```
pip install django-filter;
```
```python
INSTALLED_APPS = [
    'django_filters',
]
```
- #### [django-import-export](https://django-import-export.readthedocs.io/en/latest/index.html)
```
pip install django-import-export;
```
```python
INSTALLED_APPS = (
    'import_export',
)
```







### Other projects

Check out the other stuff I've worked upon.

- **_AI/ML/Data Science_**

  - **AML-Home-Credit-Default-Risk** : [Predicting how capable each applicant is of repaying a loan \(Kaggle Challenge\).](https://github.com/Kiran-Karandikar/AML-Home-Credit-Default-Risk)

  - **Exercise-performance-analysis** : [Prototype exercise volume prediction using machine learning models.](https://github.com/Kiran-Karandikar/Exercise-performance-analysis)

- **_Web Development_**

  - **flask-app-template** : [Simple, reusable, minimalistic, configurable flask app.](https://github.com/Kiran-Karandikar/flask-app-template)

  - **flask-oauth2-wrike-api** : [A sample Flask app to authenticate with Wrike as a third-party OAuth2 provider.](https://github.com/Kiran-Karandikar/flask-oauth2-wrike-api)

> Section `Other projects` is auto-updated using [Github actions](https://github.com/features/actions).

<!-- CONTACT -->

## Contact

- [Kiran Karandikar:](mailto:connect.funnel.github@kirankarandikar.com)

