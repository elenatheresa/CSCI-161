'''
elena corpus
program 3 
CSCI 161
'''

#Part 1
print("Part 1")
minNum = int(input("enter a minimum number: "))
maxNum = int(input("enter a maximum number: "))

#assert syntax 
assert maxNum > minNum, "enter a maximum value: "

#print odd numbers between the two values
print("Odd Numbers between", minNum, "and", maxNum)
for i in range(minNum,maxNum + 1):
    if (i % 2 != 0):
        print(i)

#print the prime numbers between the two values
print("Prime numbers between", minNum, "and",maxNum)
for num in range(minNum,maxNum + 1):
    if num > 1:
        for n in range(2,num):
            if (num % n) == 0:
                break
        else:
            print(num)    
    
#print the numbers ranged incremting by 2 and multiples of 3
print("Values incrementing by 2 and multiples of 3 between the range of", minNum, "and", maxNum)
for x in range(minNum, maxNum + 1):
    if x > 0:
        if x % 2 == 0:
            if x % 3 == 0:
                print(x)

#Part 2
print()
print("Part 2")
theList = [9, 3, 6, 2, 10, 6, 3, 29, 11]
sumOfList = 0

for number in theList:
    if number == 5:
        break
    else:
        sumOfList = sumOfList + number
        
print("The sum of the list is:", sumOfList)
