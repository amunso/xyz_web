from django.urls import path
from django.views.generic.edit import CreateView

from .views import MainView, VoteView, confirm, ApproveContributionView
from .models import Contribution, Vote

urlpatterns = [
    path('', MainView.as_view()),
    path('vote/', VoteView.as_view(), name='vote'),
    path('add/', CreateView.as_view(
        model=Contribution,
        fields=['name', 'contact_email', 'video_link', 'description'],
        success_url='/'
    ), name='add'),
    path('approve/', ApproveContributionView.as_view()),
    path('confirm/<token>/', confirm),
]
