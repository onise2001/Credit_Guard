from rest_framework.test import APITestCase, APIClient
from django.test import TestCase
from rest_framework import status
from .models import Card
from django.contrib.auth.models import User
from django.urls import reverse
from .serializers import CardSerializer
import time, random, string

# Create your tests here.

class TestCardModel(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.test_user = User.objects.create(username='test_user', password='123456789', email='test@gmail.com')
        self.client.force_authenticate(user=self.test_user)
        self.test_item = Card.objects.create(title='Test Card', is_valid=True, censored_number='1010********1010')
        self.list_create_url = reverse('cardsviewset-list')

        self.valid_card = {
            "title": "Test valid card",
            "card_number": "1012101210121012",
            "ccv": "100",

        }

        self.invalid_card = {
            "title": "Test invalid card",
            'card_number': '1122334455667788',
            'ccv': '103'
        }

    def test_get_card_list(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_card_creation(self):
        response = self.client.post(self.list_create_url, self.valid_card ,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_invalid_card(self):
        response = self.client.post(self.list_create_url, self.invalid_card ,format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    




class TestCardSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.create(username='testuser', password='test1234', email='test@gmail.com')
        self.client.force_authenticate(user=self.test_user)
        self.list_create_url = reverse('cardsviewset-list')

        self.card = {
            'title': 'Test Card',
           
        } 

        

    def test_serializer_validation(self):
        
        card_numbers = [''.join(random.choices(string.digits, k=16)) for _ in range(0, 100)]
        ccvs = [''.join(random.choices(string.digits, k=3)) for _ in range(0, 100)]
      
        response = self.client.post(self.list_create_url, self.card,format='json')
        elapsed_time = 0
        for index in range(len(card_numbers)):
            self.card['card_number'] = card_numbers[index]
            self.card['ccv'] = ccvs[index]
            start_time = time.time()
            response = self.client.post(self.list_create_url, self.card,format='json')
            end_time = time.time()
            elapsed_time += end_time - start_time
        
        self.assertLess(elapsed_time, 1, "It took too long to validate card numbers")


         