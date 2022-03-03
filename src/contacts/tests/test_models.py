from rest_framework.test import APITestCase
from src.contacts.models import Contact
from src.users.models import User

class TestContactModel(APITestCase):

    @classmethod
    def setUpTestData(self):
        self.test_user = User.objects.create(
            id=1, username="zulu", password="123456"
        )
        
        self.contact_data = Contact.objects.create(
            owner=self.test_user,
            contact_image="https://images.unsplash.com/photo-1515658323406-25d61c141a6e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=709&q=80",
            first_name="zuluking", 
            last_name="bantu",
            country_code=254,
            phone_number=715689414,
            is_favorite=False
            )     
    
    def test_contact_model_str(self):   
        self.assertEqual(str(self.contact_data.first_name), "zuluking")

    def test_contact_has_an_owner_first_name(self):
        self.assertEqual(self.contact_data.owner, self.test_user)
        self.assertEquals(self.contact_data.country_code, 254)

