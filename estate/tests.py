from django.test import TestCase

from estate.models import *

class ModelTestCase(TestCase):

    def test_valid_user(self):
        property=Property.objects.create(property_name="abc",price=1500,property_detail="This is very good")

        self.assertTrue(property.valid_user())
    
    def test_customer_valid_phone(self):
        customer=Customer.objects.create(customer_name="Dup Raja",customer_address="Ktm City",customer_phone=987654321,customer_details="Very Good Fellow")
        self.assertTrue(customer.valid_phone())
    
    def test_valid_address(self):
        admin=Admin.objects.create(admin_name="Dup Raja",admin_address="Ktm City",admin_phone=987654321,admin_details="Very Good Fellow")
        self.assertTrue(admin.valid_address())
    
    def test_owner_valid_phone(self):
        owner=Owner.objects.create(owner_name="Dup Raja",owner_address="Ktm City",owner_phone=987654321,owner_details="Very Good Fellow")
        self.assertTrue(owner.valid_phone())
