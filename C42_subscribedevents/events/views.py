from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from . import models


class JSONResponse(HttpResponse):

    """Docstring for JSON. """

    def __init__(self, data, **kwargs):
        """ """
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# Create your views here.
@api_view(['GET'])
def subscribed_events_detail(request, id):
    if request.method == 'GET':
        event = models.Event(id)
        subscribedEvents = models.SubscribedEvents(id)
        events = subscribedEvents.getSubscribers()
        response_object = {
            'id': event.id,
            'title': event.title,
            'subscribers': events
        }
        return JSONResponse(response_object)
