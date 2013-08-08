# Django tutorial project

This is the product of my working through the
[excellent Django tutorial](https://docs.djangoproject.com/en/1.5/intro/), with some
extra playing around that I did.

To run it, on a Unix box, create an empty directory, cd into it, clone this
repository, and then run:

```bash
virtualenv myenv
. myenv/bin/activate
cd django-tutorial
./manage.py runserver 0.0.0.0:8000  # or whatever port you want
```

The "0.0.0.0" tells it to accept connections from other hosts.  By default,
it only accepts connections from localhost.

