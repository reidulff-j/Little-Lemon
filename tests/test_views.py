from django.test import TestCase
from django.core import serializers
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(ID=1, Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(ID=2, Title="Salad", Price=39.99, Inventory=37)
        Menu.objects.create(ID=3, Title="Chicken", Price=47.89, Inventory=18)
    
    def test_getall(self):
        items = serializers.serialize('json', Menu.objects.all())
        expected_items='[{"model": "restaurant.menu", "pk": 1, "fields": {"Title": "IceCream", "Price": "80.00", "Inventory": 100}}, {"model": "restaurant.menu", "pk": 2, "fields": {"Title": "Salad", "Price": "39.99", "Inventory": 37}}, {"model": "restaurant.menu", "pk": 3, "fields": {"Title": "Chicken", "Price": "47.89", "Inventory": 18}}]'
        
        self.assertEqual(items, expected_items)