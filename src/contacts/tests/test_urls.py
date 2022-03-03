from django.urls import reverse, resolve
from django.test import SimpleTestCase
from src.contacts.views import ContactListView, ContactDetailView



class ContactsAPIUrlsTests(SimpleTestCase):

    def test_landing_page_is_resolved(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_get_contacts_is_resolved(self):
        url = reverse('contacts_app:contact-list')
        self.assertEquals(resolve(url).func.view_class, ContactListView)

    def test_get_contact_detail_is_resolved(self):
        url = reverse('contacts_app:contact-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, ContactDetailView) 

    