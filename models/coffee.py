

class Coffee:

    def __init__(self,name): # initiatiates an instance where name is defined and the list access modifier is defined

        self.name = name 
        self.__orders = [] 

    
    @property
    def name(self):  # getter method for name and name attribute is privated
        return self.__name  

    
    @name.setter
    def name(self,coffee_name): #  validates if the name is a string and is 3 characters long
        if isinstance(coffee_name,str) and len(coffee_name) >= 3:
            self.__name = coffee_name

        else:
            raise ValueError("Name must be a string and 3 characters long")

     
    

    def customers(self):
        return list({order.customer for order in self.__orders})

    
    def orders(self): 
        return self.__orders 



    def add_order(self,order): # creates a new order and appendeds to the list of orders 
        self.__orders.append(order)


    def average_price(self):  # returns the average price for a coffee based on orders
        if len(self.__orders) == 0:
            return 0

        return sum(order.price for order in self.__orders) / len(self.__orders)
      

    def num_orders(self):#returns the total number of orders
        return len(self.__orders) 


    def __repr__(self):
        return f"Coffee({self.name})"
       

            