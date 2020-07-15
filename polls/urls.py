from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [

    path('', views.PollsListView.as_view(), name='home'),
    #path('1/', views.add_vote),
    path('1/', views.PollsDetailView.as_view(), name='detail'),

    path('<slug:slug>/result/', views.ResultDetailView.as_view(), name='result'),


]
