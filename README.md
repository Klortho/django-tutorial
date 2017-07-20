# Django tutorial project

This is the product of my working through the
[Django tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/).

***This from-scratch branch is a re-do, since a lot of things have changed.***

To run it:

```bash
virtualenv -p python3 venv
. env/bin/activate
pip install -r requirements.txt
./manage.py runserver
```

Then go to [http://localhost:8000/]().


To start the server such that it allows connections from other machines:

```
./manage.py runserver 0.0.0.0:8000
```


## Steps

```
virtualenv -p python3 venv
. venv/bin/activate
```

Created requirements.txt with the single line: `Django`.

```
pip install -r requirements.txt
django-admin startproject mysite .
python manage.py runserver
```

Loaded http://localhost:8000 in the browser, and got "It worked!".
