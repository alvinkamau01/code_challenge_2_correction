
from models.orders import Order


class Customer:

    def __init__(self,name):# constructor. The attributes are defined 
        self.name = name  
        self.__orders = [] 

    @property # gets the name attribute and changes it to a property
    def name(self):
        return self.__name  


    @name.setter  # checks if the name attribute fulfills given conditions
    def name(self,name):
        if isinstance(name,str) and 1 <= len(name) <= 15:
            self.__name = name

        else:
            raise ValueError ("Name must be a string and between 1 and 15 characters")

    
    def orders(self): # instantiates orders method
        return self.__orders 


    def coffees(self):  # iterates over the list of coffee
        return list({order.coffee for order in self.__orders})




    def create_order(self,coffee,price): # creates  a new order and adds it to the list of orders
        order = Order(self,coffee,price) 

        self.__orders.append(order) 
        coffee.add_order(order)
        return order

    @staticmethod # returns the customer who spent the most
    def most_aficionado(coffee):
        max_spent = 0
        highest_customer = None 
        for customer in {order.customer for order in coffee.orders()}:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                highest_customer = customer

        return highest_customer
   

    def __repr__(self):
        return f"Customer: {self.name}"