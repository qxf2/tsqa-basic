"""
Write a program to create a shopping cart in which you can add the items and quantity, 
update the quantity and remove an item from the list.
"""
from shopping_cart_module import ShoppingCart

class Item(): 
    "Get the items to be added into the shopping cart"
    def __init__(self,item_name,item_quantity):
        self.item_name = item_name
        self.item_quantity = item_quantity
                
# Program starts here
if __name__ == "__main__":
    # item1 is an object of class Item
    item1 = Item('Sugar',1)
    item2 = Item('Salt',2)
    item3 = Item('Banana',1)

    # cartobject is an object of the shopping cart class
    cartobject = ShoppingCart()
    shopping_list = cartobject.add_item(item1)
    print("Added the first item in the list",shopping_list)

    shopping_list = cartobject.add_item(item2)
    print("Added the second item in the list",shopping_list)

    shopping_list = cartobject.add_item(item3)
    print("Added the third item in the list",shopping_list)

    item4 = Item('Banana',3)
    shopping_list = cartobject.add_item(item4)
    print("Added the fourth item in the list",shopping_list)

    shopping_list = cartobject.remove_item(item2)
    print("Removed an item from the list",shopping_list)