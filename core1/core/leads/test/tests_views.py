from django.test import TestCase

# Create your tests here.

from django.shortcuts import reverse


class home(TestCase):
    
    def test_status_code(self):
        response = self.client.get(reverse("leads:home"))
        # print(response.content)
        # print(response.status_code)
        # to make sure the test always bring 200
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

