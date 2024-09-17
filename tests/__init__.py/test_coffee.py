import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import pytest

from models.customers import Customer
from models.coffees import Coffee
from models.orders import Order


def test_create_coffee():
    coffee = Coffee("Expressos") 
    assert coffee.name == "Expressos"



def test_coffee_orders(): 
    customer = Customer("Sophie") 
    coffee = Coffee("Expressos") 
    order = customer.create_order(coffee,5) 

    assert coffee.num_orders() == 1 
    assert coffee.average_price() == 5.0