# Create your views here.

from django.http import HttpResponse
import os


def home(request):
    return HttpResponse(
"""
<html>
<body>
<h1>Django tutorial project</h1>
<p>
""" +
        "__file__ = " + __file__ + "<br/>\n" +
        "  SITE_HOME = " +
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "<br/>\n"
        "</p>\n" +
"""
<p>
  Entry points:
</p>
<ul>
  <li><a href='admin/'>admin/</a></li>
  <li><a href='polls/'>polls/</a></li>
</ul>
</body>
</html>
"""
    )

