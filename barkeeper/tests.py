from django.test import TestCase
from models import Event

class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(
            created="2018-11-20T15:58:44.767594-06:00",
            text="Stawberry",
            weight=71.21,
            result=1)