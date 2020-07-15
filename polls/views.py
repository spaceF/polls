from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Polls, Persons
from .forms import VotesForm


class PollsListView(ListView):
    """Список активных голосований"""
    model = Polls
    queryset = Polls.objects.all()
    template_name = "poll_temp/polls_list.html"
    context_object_name = "list_polls"


class PollsDetailView(DetailView):
    """Подробная информация о голосовании"""
    model = Polls
    template_name = "poll_temp/test.html"
    context_object_name = "detail_polls"
    slug_field = "url"


class ResultDetailView(DetailView):
    """Результаты голосования"""
    model = Polls
    template_name = "poll_temp/polls_result.html"
    context_object_name = "result_polls"
    slug_field = "url"


#class AddVote(View):
 #   """Голосование"""
  #  def post(self, request, pk):
   #     form = VotesForm(request.POST)
    #    polls = Polls.objects.get(pk=pk)
     #   if form.is_valid():
            # form = form.save(commit=False)
            # person = polls.persons_set.get(pk=request.POST["votes"])
            # person.votes += 1
            # person.save()
      #      return redirect(polls.get_absolute_result_url())
       # return HttpResponse(status=400)

def add_vote(request):
    form = VotesForm()
    return render(request, "poll_temp/test.html", {'form': form})
