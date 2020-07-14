from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.PollsListView.as_view()),
    path('<slug:slug>/', views.PollsDetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultDetailView.as_view(), name='result'),
]
