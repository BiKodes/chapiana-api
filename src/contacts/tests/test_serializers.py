from rest_framework.test import APITestCase
from src.contacts.models import Contact
from src.contacts.serializers import ContactSerializer, CreateContactSerializer
from src.users.models import User

class TestContactSerializer(APITestCase):

    def setUp(self):
    
        self.test_user=User.objects.create(
            id=1, username="zulubantu", password="123456"
            )
        
        self.contact_data={
            "owner":self.test_user,
            "contact_image":"https://images.unsplash.com/photo-1515658323406-25d61c141a6e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=709&q=80",
            "first_name":"zulu",
            "last_name":"bantu",
            "country_code":254,
            "phone_number":715689414,
            "is_favorite":False
        }

        self.serializer_data = {
            "owner":self.test_user,
            "contact_image":"https://images.unsplash.com/photo-1515658323406-25d61c141a6e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=709&q=80",
            "first_name":"bantu",
            "last_name":"bantu",
            "country_code":254,
            "phone_number":722000000,
            "is_favorite":False
        }

        self.contact = Contact.objects.create(**self.contact_data)
        
        self.serializer = ContactSerializer(instance=self.contact)

    def tearDown(self):
        return super().tearDown()

    def test_contact_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(set(data.keys()), 
                        set(['owner', 'contact_image', 'first_name', 'last_name', 'country_code',
                            'phone_number', 'is_favorite']))

    def test_contact_serializer_with_empty_data(self):
        serializer = ContactSerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_contact_serializer_produces_expected_data_for_fields(self):
        data = self.serializer.data
        self.assertEqual(data['first_name'], self.contact_data['first_name'])

    def test_contact_serializer_country_code_lower_bound(self):
        self.serializer_data['country_code'] = 200

        serializer = ContactSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        # self.assertEqual(set(serializer.errors), set(['country_code']))

    def test_contact_serializer_country_code_upper_bound(self):
        self.serializer_data['country_code'] = 447

        serializer = ContactSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        # self.assertEqual(set(serializer.errors), set(['country_code']))

    def test_contact_serializer_with_valid_data(self):
        serializer = self.contact_data
        self.assertTrue(serializer.is_valid())

class TestCreateContactSerializer(APITestCase):

    @classmethod
    def setUpTestData(self):
        
        self.test_user=User.objects.create(
            id=1, username="zulubantu", password="123456"
            )
        
        self.contact_data={
            "owner":self.test_user,
            "contact_image":"https://images.unsplash.com/photo-1515658323406-25d61c141a6e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=709&q=80",
            "first_name":"zulu",
            "last_name":"bantu",
            "country_code":254,
            "phone_number":715689414,
            "is_favorite":False
        }

        self.contact = Contact.objects.create(**self.contact_data)
        
        self.serializer = CreateContactSerializer(instance=self.contact)

    def test_createcontact_serializer_has_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(set(data.keys()), 
                        set(['id' ,'owner', 'contact_image', 'first_name', 'last_name', 'country_code',
                            'phone_number']))

    def test_createcontact_serializer_creates_serializers(self):
        data = self.serializer.data
        self.assertTrue(dict(data), self.contact_data)
        self.assertEqual(data.values(['715689414'], self.contact_data['715689414']))
        