

class Order:

    def __init__(self,customer,coffee,price): # Initializes  the order with customer, coffee and price
        self.customer = customer
        self.coffee = coffee
        self.price = price


    @property # gets value of customer and privates it
    def customer(self):
        return self.__customer 

    @customer.setter # sets the customer but checks if it is an instance of customers class first
    def customer(self,cust):

        from models.customers import Customer 
        if isinstance(cust,Customer): 
            self.__customer = cust

        else:
            raise ValueError("Invalid coffee")

    @property
    def coffee(self): # gets value of coffee and privates it
        return self.__coffee
    
    @coffee.setter
    def coffee(self,coffee):  # checks if coffee is an instance of Coffee  if true it add
        from models.coffees import Coffee
        if isinstance(coffee,Coffee):
            self.__coffee = coffee

        else:
            raise ValueError("Invalid coffee")


    @property
    def price(self): #retrieves the attribute price and privates it
        return self.__price


    @price.setter
    def  price(self,price): #setters check if the price is between 1 and 10
        if 1.0 <= price <= 10.0:
            self.__price = price
        
        else:
            raise ValueError("Price must be between 1.0 and 10.0")


    def __repr__(self):
        return f"Order---> Customer: {self.customer.name},Coffee: {self.coffee.name},Price: {self.price}"