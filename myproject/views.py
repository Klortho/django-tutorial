# Create your views here.

from django.http import HttpResponse
import os
import requests
from xml.etree import ElementTree


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
  <li><a href='eutils/'>eutils/</a> - example of fetching and parsing E-utilities XML</li>
</ul>
</body>
</html>
"""
    )

def eutils(request):
    response = requests.get(
        'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',
        params={'db':'pubmed', 'term':'1[geneid]'}
    )
    pubmed_el = ElementTree.fromstring(response.content)
    id_xpath = pubmed_el.findall('.//IdList/Id')
    r = ""
    for id_el in id_xpath:
        r += id_el.text + "\n"

    return HttpResponse(r, content_type="text/plain")