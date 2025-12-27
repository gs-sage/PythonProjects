# creating an order class with a dunder function that checks if an order price is greater than another

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, second_obj):
        first_obj_price = self.price
        second_obj_price = second_obj.price
        if(first_obj_price > second_obj_price):
            return f"{self.item}(${self.price}) is greater than {second_obj.item}(${second_obj.price})"
        else:
            return f"{second_obj.item}(${second_obj.price}) is greater than {self.item}(${self.price})"
        
ord1 = Order("Pizza", 15)
ord2 = Order("Sub", 11)

check_price = ord1 > ord2
print(check_price)
