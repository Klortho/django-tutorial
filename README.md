# Django tutorial project

For Django 1.11 and Python 3.4, or later.

This is the product of my working through the
[Django tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/).
The 'old' branch has a version that I had gotten much further with, on an
earlier version of Django. It doesn't work with the newer Django.

***This from-scratch branch is a re-do, since a lot of things have changed.***

To run it:

```bash
virtualenv -p python3 venv
. env/bin/activate
pip install -r requirements.txt
./manage.py runserver
```

Then go to [http://localhost:8000/]() for the top-level page, or
[http://localhost:8000/polls/]() for the "polls" app.


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

***Then committed 84351a3.***

Started a new app with `./manage.py startapp polls`.

Edited mysite/urls.py:

```python
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
```

Created polls/urls.py:

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

Edited polls/views.py to this:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

Brought up http://localhost:8000/polls/, and saw this view.
