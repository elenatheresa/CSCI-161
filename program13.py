'''
elena corpus
program 13
csci 161
linear search : the search that questions the values in the list one by one
'''

class Node:

   def __init__(self, data, nextNode=None):
       #contain the data
       self.data = data
       #point to the next node in the linked list 
       self.nextNode = nextNode

   def getData(self):
       #used to get the data for the list 
       return self.data

   def setData(self,val):
       #once recieved the data, we are setting the data we recieved from the values we got 
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

   def __init__(self, head = None):
       #head is most recently added node
       self.head = head
       #size is the number of values in the list 
       self.size = 0

   def getSize(self):
       #refers to finding the number of values in the list 
       return self.size

   #this function adds the node
   def addNode(self,data):
       #simpy addding the new nodes, and setting their values correctly which is what is being      
       #explained in the prior class  
       newNode = Node(data, self.head)
       self.head = newNode
       self.size += 1
       return True
     
   #this function prints the node  
   def printNode(self):
       #this is printing each of the node's data part 
       curr = self.head
       #while there are still nodes in the list we continue to print them and recieve the next one 
       while curr:
           print(curr.data)
           curr = curr.getNextNode()

   #This Function checks whether the value 
   #x present in the linked list  
   def search(self, x): 
  
        #Initialize current to head 
        current = self.head 
  
        #loop till current not equal to None 
        while current != None: 
            if current.data == x: 
                return True #data found 
              
            current = current.getNextNode()
          
        return False #Data Not found 

myList = LinkedList()

intValue = int(input("Enter an integer value for your list: "))
myList.addNode(intValue)
newValue = input("Would you like to add more values? (y or n) ")
print()
#while loop in order to contine to grow the list length
while newValue != 'n':
    intValue = int(input("Enter an integer value for your list: "))
    myList.addNode(intValue)
    newValue = input("Would you like to add more values? (y or n) ")
    print()


#section to input the value you want to find    
numInput = int(input("What number are you looking for? ")) 
numFound = myList.search(numInput)
if (numFound == False):
    print("The number is not in the list")
else:
    print("The number is in the list")

#asking if there is another number wanting to be searched for 
anotherSearch = input("would you like to search for another value? (y/n): ")
while anotherSearch != 'n':
    numInput = int(input("What number are you looking for? "))
    numFound = myList.search(numInput)
    if (numFound == False):
        print("The number is not in the list")
    else:
        print("The number is in the list")
    anotherSearch = input("would you like to search for another value? (y/n): ")
    print()
