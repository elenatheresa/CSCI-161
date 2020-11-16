''' 
Haleh Azizi
Program 10
Computer Sciences2 (CSCI2)
'''

import os
import FileUtils
class ItemToPurchase:
    def __init__ (self):
        self.item_name = ''
        self.item_description = ''
        self.item_price = 0.00
        self.item_quantity = 0
        
    def print_item_cost(self):
        totalcost = (self.item_quantity) * (self.item_price)
        print(self.item_name, self.item_quantity, '@','$',self.item_price,'=','$', totalcost)    
        
    def print_item_description(self):
        print( self.item_name,':', self.item_description) 


class ShoppingCart:
    def __init__ (self,customer_name,current_date):
     
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        
    def add_item(self, newItem):
        self.cart_items.append(newItem)
                
        
    def get_cost_of_cart(self):
        for item in self.cart_items:
            totalcost = (item.item_quantity) * (item.item_price)
            Total = Total + totalcost
        print("Total: ", Total )        
        
    def print_total(self):
        print( self.customer_name,'\'Shopping Cart\-', self.current_date)
        print( "Number of Items:" , len (self.cart_items))
        Total = 0
        for item in self.cart_items:
            totalcost = (item.item_quantity) * (item.item_price)
            print(item.item_name, item.item_quantity, '@','$',item.item_price,'=','$', totalcost)
            Total = Total + (item.item_price * item.item_quantity)
        print("Total: ", Total )
        
    def print_descriptions(self):
        print( self.customer_name,'\'Shopping Cart\-', self.current_date) 
        print( "Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
         
    def remove_item(self,itemRemove):
        for item in self.cart_items:
            if item.item_name == itemRemove:
                self.cart_items.remove(item)
            if item.item_name != itemRemove:
                print("Item not found in the cart. Nothing removed.")
            
    def modify_item(self, itemModify):
        for i  in range(len(self.cart_items)):
            if self.cart_items[i].item_name == itemModify.item_name:
                self.cart_items[i].item_quantity = itemModify.item_quantity
            if self.cart_items[i].item_name != itemModify.item_name:
                print("Item not found in the cart. Nothing modified.")
    
    def write_reciept_to_file(self):
        Total = 0
        fileName= self.customer_name
        file = open(fileName + ".txt",'w')
        file.write("---RECEIPT---\n")
        file.write(self.customer_name+"'s Shopping Cart - " + self.current_date)
        file.write("\n")
        totalquantity = 0
        for item in self.cart_items:
            totalquantity += (item.item_quantity)        
        file.write("Number of Items:" + str (totalquantity)+"\n")
        
        for x in range(len(self.cart_items)):
            for item in self.cart_items:
                totalcost = (item.item_quantity) * (item.item_price)
                file.write(str(item.item_name) + str(item.item_quantity) + '@'+'$'+ str(item.item_price) +'='+'$'+ str(totalcost)+"\n")
            
        for item in self.cart_items:    
            file.write(self.customer_name+'\'Shopping Cart\-'+ self.current_date+"\n")    
            Total = Total + (item.item_price * item.item_quantity) 
            file.write("Total: " + str(Total)+"\n") 
            
        file.write("---RECEIPT---\n")     
        file.close() 
        
    def view_reciept_file(self):
        try:
            if os.path.isfile (self.customer_name+ ".txt") == False:
                raise ValueError("Data file dose not exist")    
            else:
                with open(self.customer_name +".txt", "r") as File:
                    print (File.read())
           
                  
        except ValueError as excpt:
            
            print("File not found.")            
                 
        
        
           
def print_menu(theCart):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from the cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("f - Finalize order")
    print("v - View receipt")
    print("q - Quit")
    print()
    optionMenu = input ("Choose an option(a,r,c,i,o,f,v,q): ")    
    
    print()
    if optionMenu == "a":
        try:
            print("ADD ITEM TO CART")
            name = input("Enter the item name:")
            newItem = ItemToPurchase()
            newItem.item_name = name
            newItem.item_description  = input ("Enter item description:\n")
            
            newItem.item_price = float(input ("Enter the item price: \n"))
            if (newItem.item_price <= 0):
                raise ValueError("Price is less than or equal to 0")
            elif (int(newItem.item_price) != newItem.item_price):
                raise ValueError("Price is a float number")            
            elif (newItem.item_price ==''):
                raise ValueError("Price is a letter")                
                          
        except ValueError as excpt:
            print(excpt)
            print("Valid number")
            print_menu(theCart)
            
                       
        try:
            newItem.item_quantity = int(input ("Enter the item quantity: \n"))
            if (newItem.item_quantity <= 0):
                
                raise ValueError("Quantity is less than or equal to 0")
            
            elif (int(newItem.item_quantity) != newItem.item_quantity):
                raise ValueError("Quantity is a float number")            
            elif (newItem.item_quantity ==''):
                raise ValueError("Quantity is a letter")    
            
                          
        except ValueError as excpt:
            print(excpt)
            print("Valid number")
            
        else:
            theCart.add_item(newItem)
                   
            
    print()
    if optionMenu == "i":
        print("OUTPUT ITEMS' DESCRIPTIONS")
        #print( theCart.customer_name,'\'Shopping Cart\-', theCart.current_date)
        #print("Item Descriptions")
        theCart.print_descriptions()
                        
    print()
    if optionMenu == "o":
        print("OUTPUT SHOPPING CART")
        #print( theCart.customer_name,'\'Shopping Cart\-', theCart.current_date)
        #print("Number of Items:", len(theCart.cart_items))
        theCart.print_total()
    print()
    
    if optionMenu == "c":
        print("Change item quantity")
        item = input("Enter the item name:\n ")
        item_quantity=int(input("Enter the new quantity:"))
        chengItem = ItemToPurchase()
        chengItem.item_name = item
        chengItem.item_quantity= item_quantity
               
        theCart.modify_item(chengItem)
    print()
    
    if optionMenu == "r":
        print("REMOVE ITEM FROM CART")
        thing = input("Enter the name of the item to remove:")
        theCart.remove_item(thing)
    print()
    
    if  optionMenu == "f":
        theCart.write_reciept_to_file()
        print("RECEIPT SUCCESSFULLY WRITTEN TO FILE")
        donShopping = input("Are you sure you’re done shopping (y/n)?:")
        if donShopping == "y" or donShopping =="Y":
            exit()
        elif donShopping == "n" or donShopping =="N":
            print_menu(theCart)
            
    print()    
    if  optionMenu == "v":
        theCart.view_reciept_file()
                        
       
    return optionMenu

if __name__ == "__main__":
    customer_name = input("Enter the customer's name:")
    date = input("Enter today's date:")
    print( "Customer name:" , customer_name)
    print( "Today's date:", date)
    theCart = ShoppingCart(customer_name, date)  
    
    optionMenu=''
    while optionMenu != "q":
        optionMenu = print_menu(theCart)
