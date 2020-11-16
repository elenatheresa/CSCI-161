'''
elena corpus
program 9
csci 161
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
        items = self.cart_items[:]
        for i in range(len(items)):
            item = items[i]
            if item._name == item_name:
                del self.cart_items[i]
                count += 1
        if count == 0:
            print(" ")
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase): #try
        count = 0
        items = self.cart_items[:]
        for i in range(len(items)):
            item = items[i]
            if item.item_name == itemToPurchase.item_name:
                count += 1
                if itemToPurchase.item_description != "none":
                    item.item_description(itemToPurchase.item_description)
                try:
                    if itemToPurchase.item_price != 0:
                        item.item_price(itemToPurchase.item_price)
                except ValueError:
                    print('item must be an integer greater than 0.')
                try:
                    if itemToPurchase.item_quantity != 0:
                        item.item_quantity(itemToPurchase.item_quantity)
                except ValueError:
                    print("the quantity must be larger than 0."
                    

        if count == 0:
            print(" ")
            print("Item not found in cart. Nothing modified.")

    def get_cost_of_cart(self):
        cost = 0
        items = self.cart_items[:]
        for i in range(len(items)):
            item = items[i]
            cost += (item.item_quantity * item.item_price)
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
            self.item.print_item_cost()

        total = self.get_cost_of_cart()
        print("Total: $", str(total))

    def print_description(self):
        print(self.customer_name, "Shopping Cart -", self.current_date)
        print()
        print("Item Description")
        for items in self.cart_items:
            #print(self.items.item_name, ':', self.items.item_description())
            print(self.cart_items.item_name, ':', self.cart_items.item_description())
        if self.cart_items == 0:
            print("empty")


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
        newCust.get_cost_of_cart()
        print()
    elif menuOp == 'r':

        print()
    elif menuOp == 'c':

        print()
    elif menuOp == "q":

        print()
    
    return menuOp, itemToPurchase

cart_items = []

if __name__ == "__main__":
    '''
    print("item 1")
    name = input('Enter item name: ')
    item1 = itemToPurchase()
    item1.item_name = name
    item1.item_description = input('Enter item\'s description: ')
    item1.item_price = float(input("Enter item\'s price: "))
    item1.item_quantity = int(input("Enter item quantity: "))
    cart_items.append(item1)
    print()
    print("item 2")
    name = input('Enter item name: ')
    item2 = itemToPurchase()
    item2.item_name = name
    item2.item_description = input('Enter item\'s description: ')
    item2.item_price = float(input("Enter item\'s price: "))
    item2.item_quantity = int(input("Enter item quantity: "))
    cart_items.append(item2)
    totalCost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print()
    '''
    customer_name = input("Enter Customer\'s Name: ")
    current_date = input("Enter Current Date: ")
    newCust = ShoppingCart(customer_name, current_date)

    #cart_items.append(name)
    '''
    print()
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    print()
    print("Total:", totalCost)

    print()
    print("items descriptions")
    item1.print_item_description()
    item2.print_item_description()
    print()
    '''
menuOp = 'y'
while menuOp != 'q':
    menuOp = print_menu(newCust)

