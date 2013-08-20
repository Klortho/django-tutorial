# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Poll, Choice


class IndexView(generic.ListView):
    # Override the default template name.  By default, the list view generic
    # uses a template called <app>/<model>_list.html.
    # Inside the template, the context object will, by default, be called
    # poll_list, and it is constructed by the get_queryset() method below.
    template_name = 'polls/index.html'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Poll.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]

# This is the old, non-generic view way to do the index:
#def index(request):
#    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#    context = {'latest_poll_list': latest_poll_list}
#    return render(request, 'polls/index.html', context)



class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())





#def detail(request, poll_id):
#    poll = get_object_or_404(Poll, pk=poll_id)
#    return render(request, 'polls/detail.html', {'poll': poll})

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

#def results(request, poll_id):
#    poll = get_object_or_404(Poll, pk=poll_id)
#    return render(request, 'polls/results.html', {'poll': poll})

#---------------------------------------------------------------------
# This handles URLs that are POSTed from the form, like /polls/1/vote/.
# It will either do a 404, print the same form again with a warning, or
# (if everything works normally) redirect to the polls detail view.

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)

    try:
        selected_choice = p.choice_set.get(pk = request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


