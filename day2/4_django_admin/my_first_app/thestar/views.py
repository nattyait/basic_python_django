from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from thestar.models import Competitor, Vote
from django.db.models import Count
from django.template import RequestContext
def home(request):
    template = 'home.html'
    competitors = Competitor.objects.all().order_by('name')\
                    .annotate(vote_total=Count('votes'))\
                    .order_by('-vote_total')
    data = {'competitors': competitors}
    context = RequestContext(request, data)
    return render_to_response(template, context)

def vote(request):
    no = request.GET['no']
    competitor = Competitor.objects.get(no=no)
    vote = Vote()
    competitor.votes.add(vote)
    return HttpResponseRedirect('/')
