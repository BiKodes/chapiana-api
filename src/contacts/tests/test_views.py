from rest_framework.test import APITestCase
from django.urls import reverse
from src.contacts.models import Contact
from rest_framework import status
from src.users.models import User
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient


class ContactListAPIViewTest(APITestCase):

    contacts_url = reverse('contacts_app:contact-list')

    @classmethod
    def setUpTestData(self):
        test_user = User.objects.create(
            id=1, username="zulu", password="123456"
        )
        
        self.contact_data={
                "owner":test_user,
                "contact_image":"https://images.unsplash.com/photo-1515658323406-25d61c141a6e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=709&q=80",
                "first_name":"zulu",
                "last_name":"bantu",
                "country_code":254,
                "phone_number":715689414,
                "is_favorite":False
            }

    def tearDown(self):
        return super().tearDown()

    def test_post_contact_cannot_created_with_no_data(self):
        response = self.client.post(self.contacts_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_contact_can_be_created_with_data(self):

        response = self.client.post(
            self.contacts_url, self.contact_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 

    def test_post_contact_unathenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.post(
           self.contacts_url, self.contact_data 
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_contacts_authenticated(self):
        response = self.client.get(self.contacts_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_contacts_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.contacts_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ContactDetailAPIViewTest(APITestCase):

    @classmethod
    def setUpTestData(self):
        self.test_user = User.objects.create(
            id=1, username="zulu", password="123456"
        )

        self.contact_url = reverse('contacts_app:contact-detail', args=[1])

        self.contact_data={
                "owner":self.test_user,
                "contact_image":"https://images.unsplash.com/photo-1515658323406-25d61c141a6e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=709&q=80",
                "first_name":"zulu",
                "last_name":"bantu",
                "country_code":254,
                "phone_number":715689414,
                "is_favorite":False
            }

        Contact.objects.create(**self.contact_data)

        self.kaclient = APIClient()
        self.kaclient.force_authenticate(user=self.test_user)

    def tearDown(self):
        return super().tearDown()
        
    def test_get_contact_detail(self):
        response = self.kaclient.get(self.contact_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['phone_number'], 715689414)

    def test_update_contact_by_owner(self):
        response = self.kaclient.put(self.contact_url,
        {
            "username": "zulu", "first_name":"zulu", "last_name": "king","country_code": 254,
            "phone_number": 72564889
        
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['phone_number'], 72564889)

    def test_update_contact_by_unauthorized_user(self):
        self.random_user = User.objects.create(username="random", password="123456")
        self.kaclient.force_authenticate(user=self.random_user, token=None)
        import json
        data = {
            "first_name": "kyenyeji", 
            "last_name": "kyenyeji001",
            "country_code": 254, 
            "phone_number": 722000000
        }
        response = self.kaclient.put(
            self.contact_url,
            data,
        )
        breakpoint()

        # response = self.kaclient.put(self.contact_url, 
        #                             {
        #                                 "first_name": "kyenyeji", "last_name": "kyenyeji001",
        #                                 "country_code": 254, "phone_number": 722000000
        #                             })

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_contact_by_authenticated_user(self):
        self.client.force_authenticate(user=self.test_user)
        response = self.client.delete(self.contact_url)

        self.assertEqual(response.status_code,  status.HTTP_204_NO_CONTENT)

