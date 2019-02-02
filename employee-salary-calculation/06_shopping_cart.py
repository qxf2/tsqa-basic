"""
Write a program to create a shopping cart in which you can add the items and quantity, 
update the quantity and remove an item from the list.
"""

class Item(): 
    "Get the items to be added into the shopping cart"
    def __init__(self,item_name,item_quantity):
        self.item_name = item_name
        self.item_quantity = item_quantity

class ShoppingCart():
    "Add,update and remove the items from the shopping cart"
    def __init__(self):
        self.shopping_cart = {}       
    
    def add_item(self,item):
        "Adding and updating the items into the cart"        
        #if not self.shopping_cart.has_key(item.item_name):    had to remove this line as has_key is no longer used in python 3.x
        if not item.item_name in self.shopping_cart.keys():           
            self.shopping_cart.update({item.item_name:item.item_quantity})
        else:
            for key,value in self.shopping_cart.items(): #changed iteritems with items()
                if key == item.item_name and value == item.item_quantity:
                    print ("The item and quantity you are trying to add are in the shopping cart already,no need to add it")
                
                elif key == item.item_name and value != item.item_quantity:
                    self.shopping_cart.update({item.item_name:item.item_quantity})
                    print("The item has been updated with new quantity")

        return self.shopping_cart

    def remove_item(self,item):
        "Removing an item from the list"        
        if not self.shopping_cart:
            print("There is no shopping cart and you cant delete it")

        for key,values in self.shopping_cart.items():           #changed iteritems with items()    
            if key ==item.item_name and values == item.item_quantity:
                item_to_remove = key
        self.shopping_cart.pop(item_to_remove)
        
        return self.shopping_cart     
                
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

    item5 = Item('Sugar',1)
    shopping_list = cartobject.add_item(item5)
    print("Added the fifth item in the list",shopping_list)