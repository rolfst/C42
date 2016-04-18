import unittest
from django.test import RequestFactory
from django.core.urlresolvers import reverse
import httpretty
from C42_subscribedevents.events.test.stubs import stubs
from C42_subscribedevents.events.views import subscribed_events_detail


# Create your tests here.
class SubscribedEventsViewTestCase(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.factory = RequestFactory()

    def tearDown(self):
        pass

    @httpretty.activate
    def test_subscribedEvents(self):
        self.assertTrue(httpretty.is_enabled)
        httpretty.register_uri(httpretty.GET,
                               'https://demo.calendar42.com/api/v2/events/aab8933ed99',
                               body=stubs['event'],
                               content_type='application/json'
                               )
        httpretty.register_uri(httpretty.GET,
                               'https://demo.calendar42.com/api/v2/event-subscriptions/?event_ids=[1]',
                               body=stubs['event_subscriptions'],
                               content_type='application/json')
        url = reverse('subscribed_event', args=['aab8933ed99'])
        request = self.factory.get(url)
        response = subscribed_events_detail(request, id='aab8933ed99')
        self.assertEqual(response.status_code, 200)
