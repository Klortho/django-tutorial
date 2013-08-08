# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from polls.models import Poll
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
import os


def home(request):
    return HttpResponse(
        "<h1>Django tutorial project</h1>" +
        "<p>\n" +
        "  __file__ = " + __file__ + "<br/>\n" +
        "  SITE_HOME = " +
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")) + "<br/>\n"

    )

