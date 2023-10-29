from django.shortcuts import make_toast
from django.test import SimpleTestCase


class MakeToastTests(SimpleTestCase):
    def test_make_toast(self):
        """
        Test that make_toast() returns a valid response.
        """
        self.assertEqual(make_toast(), "Here's your toast")
