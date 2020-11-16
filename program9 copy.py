'''
elena corpus
csci 161
program 10
'''


class itemToPurchase():

    def __init__(self):
        self.item_name = ''
        self.item_description = ''
        self.item_price = 0.00
        self.item_quantity = 0

    def print_item_cost(self):
        itemTotalCost = self.item_quantity * self.item_price
        print(self.item_name, self.item_quantity, '@ $', self.item_price, '=', itemTotalCost)

    def print_item_description(self):
        print(self.item_name, ':', self.item_description)


class ShoppingCart():

    def __init__(self, name = "none", date = 'March 25 2019'):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item(self, newItem): #try
        self.cart_items.append(newItem)

    def remove_item(self, item_name):
        count = 0
        for i in self.cart_items:
            item = items[i]
            if i.item_name == item_name:
                del i
                count += 1
        if count == 0:
            print(" ")
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase): #try
        count = 0
        for i in self.cart_items:
            count += 1
            if (i.item_description != "none") and (i.item_price != 0) and (i.item_quantity != 0):
                newQuantity = int(input("enter the new quantity: "))
                i.item_quantity = newQuantity

        if count == 0:
            print(" ")
            print("Item not found in cart. Nothing modified.")

    def get_cost_of_cart(self):
        print(self.customer_name, "'s Shopping Cart - ", self.current_date)
        cost = 0
        for i in self.cart_itmes:
            cost += (i.item_quantity * i.item_price)
        return cost

    def print_total(self):
        print(self.customer_name, "'s Shopping Cart - ", self.current_date)
        count = len(self.cart_items)
        if count == 0:
            print()
            print("SHOPPING CART IS EMPTY")
        return 0

        print("Number of items : ", str(count))
        print()

        for item in self.cart_items:
            item.print_item_cost()

        total = self.get_cost_of_cart()
        print("Total: $", str(total))

    def print_description(self):
        print(self.customer_name, "Shopping Cart -", self.current_date)
        print()
        print("Item Description")
        for items in self.cart_items:
            items.print_item_description()
        

def print_menu(items):
    customer_cart = newCust
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from the cart")
    print("c - Change item quantity")
    print("i - Output items\' descriptions")
    print("o - Output Shopping Cart")
    print("q - Quit")
    print()
    menuOp = input("Choose an option from the menu: ")
    while (menuOp != 'a') and (menuOp !='i' ) and (menuOp != 'o') and (menuOp != 'q') and (menuOp != 'r') and (menuOp !='c'):
        print('Enter a valid value')
        menuOp = input("Choose an option from the menu: ")
    if menuOp == 'a':
        try:
            name = input("Enter Item Name: ")
            newItem = itemToPurchase()
            newItem.item_name = name
            newItem.item_description = input('Enter item\'s description: ')
            newItem.item_price = float(input("Enter item\'s price: "))
            newItem.item_quantity = int(input("Enter item quantity: "))
            newCust.add_item(newItem)

            print()
        except ValueError:
            print("item quantity must be a integer greater than 0.")
            
    elif menuOp == "i":
        print("Output Item\'s Descriptions")
        customer_cart.print_description()
        print()
    elif menuOp == "o":
        print("Output Shopping Cart")
        customer_cart.print_total()
        print()
    elif menuOp == 'r':
        print("REMOVE ITEM FROM CART")
        item_name = input("Enter the item name: ")
        customer_cart.remove_itme(item_name)
        print()
    elif menuOp == 'c':
        print("CHANGE ITEM QUANTITY")
        item_name = input("Enter the item name: ")
        customer_cart.modify_item(item_name)
        print()
    
    return menuOp

cart_items = []

if __name__ == "__main__":
    customer_name = input("Enter Customer\'s Name: ")
    current_date = input("Enter Current Date: ")
    newCust = ShoppingCart(customer_name, current_date)

menuOp = 'y'
while menuOp != 'q':
    menuOp = print_menu(newCust)
