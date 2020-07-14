from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Polls, Persons


class PollsListView(ListView):
    """Список голосований"""

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


