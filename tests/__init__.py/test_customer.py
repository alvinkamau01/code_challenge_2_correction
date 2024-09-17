import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))




import pytest

from models.customers import Customer
from models.coffees import Coffee
from models.orders import Order

def test_create_customer():
    customer = Customer("Sophie") 
    assert customer.name == "Sophie"



def test_create_order(): 
    customer = Customer("Sophie")
    coffee = Coffee("Expressos")
    order = customer.create_order(coffee,5)


    assert len(customer.orders()) == 1
    assert customer.orders()[0].price == 5.0
    assert customer.coffees()[0] == coffee 

