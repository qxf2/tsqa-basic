class ShoppingCart:
    "Add,update and remove the items from the shopping cart"
    def __init__(self):
        self.shopping_cart = {}       
    
    def add_item(self,item):
        "Adding and updating the items into the cart"        
        if item.item_name not in self.shopping_cart.keys():
            self.shopping_cart.update({item.item_name:item.item_quantity})
        else:
            for key,value in self.shopping_cart.items():
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
        for key,values in self.shopping_cart.items():               
            if key ==item.item_name and values == item.item_quantity:
                item_to_remove = key
        self.shopping_cart.pop(item_to_remove)
        
        return self.shopping_cart     