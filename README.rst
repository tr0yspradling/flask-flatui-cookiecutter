Flat-UI Flask Project
=====================

A Flask template for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter


Use it now
----------
First please visit `Django Secret Key Generator <https://www.miniwebtool.com/django-secret-key-generator/>`_. Grab the secret key to use with the cookiecutter prompt.

Next install cookiecutter & run the generator:
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/tr0yspradling/flask-flatui-cookiecutter.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.


Features
--------

- `Bootstrap 4 <https://v4-alpha.getbootstrap.com/>`_ and `Font Awesome 4 <http://fontawesome.io/>`_ based starter template.
- `FlatUI <https://designmodo.github.io/Flat-UI/>`_ themed.
- Uses `jQuery 3 <https://jquery.com/>`_.
- Pre-configured production ready `NGINX <https://nginx.org/en/>`_ configuration with `Let's Encrypt SSL <https://letsencrypt.org/>`_.
- Flask-SQLAlchemy with basic User model.
- Easy database migrations with Flask-Migrate.
- Flask-WTForms with login and registration forms.
- Flask-Login for authentication.
- Flask-Bcrypt for password hashing.
- Procfile for deploying to a PaaS (e.g. Heroku).
- pytest and Factory-Boy for testing (example tests included).
- Flask's Click CLI configured with simple commands.
- CSS and JS minification using Flask-Assets.
- Optional bower support for frontend package management.
- Caching using Flask-Cache.
- Useful debug toolbar.
- Utilizes Flask's best practices.
