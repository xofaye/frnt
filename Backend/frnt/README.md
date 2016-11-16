# FrnT

Built with [Python 3.X][0] using the [Django Web Framework][1].

## Installation

### Requirements

* Python 3
* Node.js

### Quick start

To set up a development environment quickly, first install Python 3.4. It
comes with virtualenv built-in. So create a virtual env by:

    $ virtualenv --prompt="(frnt)" -p python3.X .virtualenv
    $ source .virtualenv/bin/activate

Install all dependencies:

    pip3 install -r requirements.txt

Run migrations:

    python3 manage.py makemigrations main
    python3 manage.py migrate

Create a superuser *(optional)*:

    python3 manage.py createsuperuser

Start up the dev server:

    python3 manage.py runserver

### Development

Make sure node.js is installed (you have the `npm` command available).

Install all npm dependencies:

    npm install

### Detailed instructions

Take a look at the docs for a detailed instructions guide.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/