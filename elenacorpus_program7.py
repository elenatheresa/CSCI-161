'''
elena corpus
csci 161
program 7
'''


class itemToPurchase():
    def __init__(self):
        self.item_name = ' '
        self.item_description = ' '
        self.item_price = 0.00
        self.item_quantity = 0

    def print_item_cost(self):
        itemTotalCost = self.item_quantity * self.item_price
        print(self.item_name, self.item_quantity, '@', self.item_price, '=', itemTotalCost)

    def print_item_description(self): 
        print(self.item_name, ':', self.item_description)



if __name__ == "__main__":
    print("item 1")
    name = input('Enter item name: ')
    item1 = itemToPurchase() 
    item1.item_name = name 
    item1.item_description = input('Enter item\'s description: ')
    item1.item_price = float(input("Enter item\'s price: "))
    item1.item_quantity = int(input("Enter item quantity: "))
    print()
    print("item 2")
    name = input('Enter item name: ')
    item2 = itemToPurchase()
    item2.item_name = name 
    item2.item_description = input('Enter item\'s description: ')
    item2.item_price = float(input("Enter item\'s price: "))
    item2.item_quantity = int(input("Enter item quantity: "))
    totalCost = (item1.item_price * item1.item_quantity) + (item1.item_price * item1.item_quantity)

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

