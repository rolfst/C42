from django.conf.urls import patterns, url
from . import views

urlpatterns = [
  url(r'^event-with-subscriptions/(?P<id>[a-z0-9_]+)', views.subscribed_events_detail, name='subscribed_event'),
]
