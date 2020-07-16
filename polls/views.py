from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.utils import timezone

from .forms import AddVoteForm
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


class AddVoteView(View):
    """Добавление голоса"""

    def post(self, request, pk):
        form = AddVoteForm(request.POST)
        poll = Polls.objects.get(pk=pk)
        if form.is_valid():
            """Выбираем кандидата за которого проголосовали"""
            selected_persons = poll.persons_set.get(pk=request.POST['person'])
            if check_active_poll(poll, selected_persons):
                selected_persons.votes += 1
                selected_persons.save()
            else:
                """Завершаем голосование"""
                poll.active = 0
                poll.save()
            return redirect(poll.get_absolute_result_url())
        return redirect("/")


def vote(request, pk):
    poll = get_object_or_404(Polls, pk=pk)
    try:
        selected_persons = poll.persons_set.get(pk=request.POST['person'])
        # print(selected_persons)
        print(request.POST)
    except (KeyError, Persons.DoesNotExist):
        return HttpResponseRedirect(poll.get_absolute_url())
    else:
        selected_persons.votes += 1
        selected_persons.save()

        return HttpResponseRedirect(poll.get_absolute_result_url())


def check_active_poll(poll, persons):
    """Проверка условий завершения голосования"""
    if poll.max_count_votes != 0:
        """Активировано условие выйгрыша 
        по достижению максимального кол-ва голосов"""
        if poll.max_count_votes >= persons.votes:
            pass
        else:
            return poll.max_count_votes >= persons.votes
    return poll.start < timezone.now() <= poll.finish

