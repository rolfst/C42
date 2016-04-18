import json
import sys
import requests
from django.conf import settings


token = settings.TOKEN
headers = {'Authorization': 'Token ' + token}


class objectjson(object):

    def __init__(self, json_data):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        self.json_data = json_data

    def __getattr__(self, key):
        if key in self.json_data:
            if isinstance(self.json_data[key], (list, dict)):
                return objectjson(self.json_data[key])
            else:
                return self.json_data[key]
        else:
            raise Exception('There is no json_data[\'{key}\'].'.format(key=key))

    def __repr__(self):
        out = self.__dict__
        return '%r' % (out['json_data'])


# Create your models here.
class Event(objectjson):

    """Docstring for Event. """

    def __init__(self, id):
        res = None
        res = requests.get('https://demo.calendar42.com/api/v2/events/' + id,
                          headers=headers)
        res.raise_for_status()
        jsonobject = json.loads(res.text)['data'][0]
        super().__init__(jsonobject)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class SubscribedEvents(list):

    """Docstring for SubscribedEvent. """

    def __init__(self, id, *args):
        """TODO: to be defined1.

        :id: TODO

        """
        list.__init__(self, *args)
        res = requests.get('https://demo.calendar42.com/api/v2/event-subscriptions/?event_ids=[' + id + ']',
                           headers=headers)
        res.raise_for_status()
        jsonobject = json.loads(res.text)['data']
        events = [SubscribedEvent(event) for event in jsonobject]
        for event in events:
            self.append(event)

    def getSubscribers(self):
        return list(map(self.__subscribersInfo, self))

    def __subscribersInfo(self, subscriber):
        return {'first_name': subscriber.subscriber.first_name}


class SubscribedEvent(objectjson):

    """Docstring for SubcribedEvent. """

    def __init__(self, data):
        """Class that traverses a subscribed event.

        :data: json data

        """
        super().__init__(data)
