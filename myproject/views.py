# Create your views here.

from django.http import HttpResponse
import os

# For eutils example:
import requests
from lxml import etree


#-----------------------------------------------------------
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


#-----------------------------------------------------------
# Demo of accessing an external web service (Eutilities) and processing XML data with
# XPath

_eutils_base = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
_esearch_id_xpath = etree.XPath('/eSearchResult/IdList/Id')

def eutils(request):
    gene_id = 2
    response = requests.get(_eutils_base + 'esearch.fcgi',
                            params={
                                'db':'pubmed',
                                'term':'{}[geneid]'.format(int(gene_id))
                            })
    esearch_doc = etree.fromstring(response.content)
    ids = [id_el.text for id_el in _esearch_id_xpath(esearch_doc)]
    r = ""
    for id in ids:
        r += id + "\n"

    return HttpResponse(r, content_type="text/plain")