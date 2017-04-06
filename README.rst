cookiecutter-flask
==================

A Flask template for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter


Use it now
----------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/tr0yspradling/flask-flatui-cookiecutter.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

Features
--------

- [Bootstrap 4](https://v4-alpha.getbootstrap.com/) and [Font Awesome 4](http://fontawesome.io/) with starter templates
- [FlatUI](https://designmodo.github.io/Flat-UI/)
- [jQuery 3](https://jquery.com/)
- Flask-SQLAlchemy with basic User model
- Easy database migrations with Flask-Migrate
- Flask-WTForms with login and registration forms
- Flask-Login for authentication
- Flask-Bcrypt for password hashing
- Procfile for deploying to a PaaS (e.g. Heroku)
- pytest and Factory-Boy for testing (example tests included)
- Flask's Click CLI configured with simple commands
- CSS and JS minification using Flask-Assets
- Optional bower support for frontend package management
- Caching using Flask-Cache
- Useful debug toolbar
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns

License
-------

BSD licensed.
