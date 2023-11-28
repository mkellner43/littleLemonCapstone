from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title='Ice Cream', price=5, inventory = 10)
        Menu.objects.create(title='Fried Pickles', price=10, inventory = 20)
        Menu.objects.create(title='Chips and Salsa', price=8, inventory = 30)
    
    def test_getall(self):
        client = APIClient()
        url = reverse('menu')

        response = client.get(url)
        data = response.data

        serialized_data = [
            {"id": item.id, "title": item.title, "price": item.price, "inventory": item.inventory}
            for item in Menu.objects.all()
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, serialized_data)