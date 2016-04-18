from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
  url(r'^event-with-subscriptions/(?P<id>[a-z0-9_]+)', cache_page(252)(views.subscribed_events_detail), name='subscribed_event'),
]
