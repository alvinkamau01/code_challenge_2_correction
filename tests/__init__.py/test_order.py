
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest

from models.customers import Customer
from models.coffees import Coffee
from models.orders import Order


def test_create_order(): 
    customer = Customer("Sophie")
    coffee = Coffee("Expressos")
    order = customer.create_order(coffee,5.0)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0


   