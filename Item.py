class Item():
    def __init__(self,name,price,quan=0):
        self.name=name
        self.price=price
        self.quan=quan
    def calculate_total_price(self):
        return self.price *self.quan

Item1=Item("phone",100,1)
Item2=Item("Laptop",1000,4)
print(Item1.calculate_total_price())
print(Item2.calculate_total_price())

# class Item():
#     def _init_(self,name,price,quantity=0) :
        
#         self.name=name
#         self.price=price
#         self.quantity=quantity
    
#     def calculate_total_price(self):
#         return self.price * self.quantity
    
# item1=Item("Phone",100,3)

# print(item1.calculate_total_price())

# item2=Item("laptop",1000,1)

# print(item2.calculate_total_price())