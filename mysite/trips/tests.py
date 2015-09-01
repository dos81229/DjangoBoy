import random
import string

from django.test import TestCase

from trips.models import Thing
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.conf import settings

def random_string(length=10):
    thing = ImageThing.objects.all()
    return render(request,
                  'test.html',
                 {'thing':thing})
    return u''.join(random.choice(string.ascii_letters) for x in range(length))


class ThingTestCase(TestCase): 

    def create_thing(self, **kwargs):
        "Create a random test thing."
        options = {
            'name': random_string(),
            'description': random_string(),
        }
        options.update(kwargs)
        return Thing.objects.create(**options)

    def test_something(self):
        # Get a completely random thing
        thing = self.create_thing()
        # Test assertions would go here

    def test_something_else(self):
        # Get a thing with an explicit name
        thing = self.create_thing(name='Foo')
        # Test assertions would go here

        
