from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=5, inventory=10)
        Menu.objects.create(title="Fried Pickles", price=10, inventory=20)
        Menu.objects.create(title="Chips and Salsa", price=8, inventory=30)

    def test_getall(self):
        client = APIClient()
        url = reverse("menu")

        response = client.get(url)
        data = response.data
        items = Menu.objects.all()
        serialized_data = MenuSerializer(items, many=True).data
   
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, serialized_data)
