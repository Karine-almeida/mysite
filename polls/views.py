# Create your views here.
from polls.models import Poll
from django.shortcuts import render
from djando.http import Http404


def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	try:
		poll = get_object_or_404(Poll, pk=poll_id)
	except PollDoesExist:
		raise Http404
	return render(request,'polls/detail.html', {'poll':poll})

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)  