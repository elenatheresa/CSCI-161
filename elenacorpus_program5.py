'''
elena corpus
program 5
CSCI 161
'''
#inputing title
userTitle = input('Enter a title for the data: ')
print("You entered:", userTitle)

print()

#inputing column 1 
column1 = input("Enter the column 1 header: ")
print("You entered:", column1)

print()

#inputing column 2
column2 = input("Enter the column 2 header: ")
print("You entered:", column2)

print()

#error checkind and organizing into lists
dataList = []
dataStringList = []
dataIntegerList = []
dataPoint = input("Enter a data point (enter -1 to stop input): ")
while dataPoint != "-1":
    if dataPoint == -1:
        break
    commas = dataPoint.count(',')
    if commas == 0 :
        print("Error: No commas in", dataPoint)
    elif commas > 1:
        print("Error: Too many commas in", dataPoint)
    elif commas == 1:
        myList = dataPoint.split(',')
        print(myList[1])
        #if myList[1][0].isspace():
         #   myList[1][0].strip()
        #print(myList[1])
        while (myList[1][0:].isdigit()==False and myList[1][1:].isdigit()==False):
            myList[1] = ''
            myList[1] = input("Enter a integer: ")
            print(myList)
        dataList.append(dataPoint)
        dataString = myList[0]
        dataStringList.append(dataString)
        dataInteger = myList[1] 
        dataIntegerList.append(dataInteger)
       # if !(dataInteger.isdigit()): #== int: 
        #    dataIntegerList.append(dataInteger)  
        #else: #if dataInteger != int:
        #    dataInteger = input("Enter a integer: ")
         #   dataIntegerList.append(dataInteger)        
        print('Data string:', dataString)
        print('Data Integer:', dataInteger)
    dataPoint = input("Enter a data point (enter -1 to stop input): ") 

#printing the data
print(format(userTitle, '^43s'))
print(format(column1, '20s'), '|', format(column2, '23s'))
for num in range(0,46):
    print('-', end='')
print()


for data in range(len(dataStringList)):
    print('%-21s|%23s' % (dataStringList[data], str(dataIntegerList[data])))
