from django.test import TestCase, Client
from django.urls import reverse
from .models import Subscriber

class SubscriptionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('subscribe')

    def test_subscribe_valid_email(self):
        response = self.client.post(self.url, {'email': 'test@example.com'}, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Subscriber.objects.count(), 1)

    def test_subscribe_invalid_email(self):
        response = self.client.post(self.url, {'email': 'invalid-email'}, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Subscriber.objects.count(), 0)

    def test_subscribe_duplicate_email(self):
        Subscriber.objects.create(email='test@example.com')
        response = self.client.post(self.url, {'email': 'test@example.com'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Subscriber.objects.count(), 1)