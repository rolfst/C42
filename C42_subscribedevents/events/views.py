from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from . import models


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        """ """
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# Create your views here.
@api_view(['GET'])
def subscribed_events_detail(request, id):
    if request.method == 'GET':
        try:
          event = models.Event(id)
          subscribedEvents = models.SubscribedEvents(id)
          events = subscribedEvents.getSubscribers()
          response_object = {
              'id': event.id,
              'title': event.title,
              'names': events
          }
          return JSONResponse(response_object)
        except Exception as err:
            if hasattr(err, 'response'):
                return Response(status=err.response.status_code)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
