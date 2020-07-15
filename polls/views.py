from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Polls, Persons


class PollsListView(ListView):
    """Список активных голосований"""

    model = Polls
    queryset = Polls.objects.all()
    template_name = "poll_temp/polls_list.html"
    context_object_name = "list_polls"


class PollsDetailView(DetailView):
    """Подробная информация о голосовании"""

    model = Polls
    template_name = "poll_temp/polls_detail.html"
    context_object_name = "detail_polls"
    slug_field = "url"


class ResultDetailView(DetailView):
    """Результаты голосования"""

    model = Polls
    template_name = "poll_temp/polls_result.html"
    context_object_name = "result_polls"
    slug_field = "url"


def vote(request, pk):
    poll = get_object_or_404(Polls, pk=pk)
    # print(poll)
    try:
        selected_persons = poll.persons_set.get(pk=request.POST['person'])
        # print(selected_persons)
    except (KeyError, Persons.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll_temp/polls_detail.html', {
            'poll': poll,
            'error_message': "You didn't select a persons.",
        })
    else:
        selected_persons.votes += 1
        selected_persons.save()

        return HttpResponseRedirect(poll.get_absolute_result_url())