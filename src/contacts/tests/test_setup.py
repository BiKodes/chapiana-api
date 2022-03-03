from rest_framework.test import APITestCase

from src.users.models import User

class TestSetUp(APITestCase):
    
    def setUp(self):

        user=User.objects.create(id=1, username="zulubantu", password="123456")
        
        self.contact_data={
            "owner":user,
            "contact_image":"https://images.unsplash.com/photo-1515658323406-25d61c141a6e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=709&q=80",
            "first_name":"zulu",
            "last_name":"bantu",
            "country_code":254,
            "phone_number":715689414,
            "is_favorite":False
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
