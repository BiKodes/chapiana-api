from django.test import SimpleTestCase
from django.urls import resolve, reverse

from src.contacts.views import ContactDetailView, ContactListView


class ChapianaAPIUrlsTests(SimpleTestCase):
    def test_landing_page_is_resolved(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_contacts_is_resolved(self):
        url = reverse("contacts_app:contact-list")
        self.assertEquals(resolve(url).func.view_class, ContactListView)

    def test_get_contact_detail_is_resolved(self):
        url = reverse("contacts_app:contact-detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, ContactDetailView)
