from django.contrib.auth.models import User
from django.test import TestCase

from .models import Incident


class IncidentContactDetailsTest(TestCase):
    def test_incident_can_store_contact_details_and_email(self):
        user = User.objects.create_user(username='tester', password='secret')

        incident = Incident.objects.create(
            title='Phishing report',
            description='Suspicious message received',
            category='Phishing',
            priority='High',
            reported_by=user,
            contact_details='0712345678',
            email='tester@example.com',
        )

        self.assertEqual(incident.contact_details, '0712345678')
        self.assertEqual(incident.email, 'tester@example.com')
