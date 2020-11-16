'''
elena corpus
program 2 
csci 161
'''

num1 = input("enter a number: ")
 
#the value is whole number 
if (num1.isdigit()):
    print("this value is a whole number")
else:
    print("this value is not a whole number")

num1 = int(num1)
# the value is, or is not, a multiple of 7 
if num1 % 7 == 0: 
    print("this value is a multiple of 7")
else: 
    print("this value is not a multiple of 7")

#the value is even or odd 
if num1 % 2 == 0: 
    print("this value is even")
else:
    print("this value is odd")

# the value is positive or negative or zero
if num1 > 0:
    print("the value is positive")
elif num1 < 0:
    print("the value is negative")
elif num1 == 0: 
    print("the value is zero")

#the value is, or is not, within range of 2010 to 2019 INCLUSIVE
if (num1 >= 2010) and (num1 <=2019):
    print("the value is within the range of 2010 and 2019")
else:
    print("the value is not within the range of 2010 and 2019")

#the value is, or is not, within the 1000 or four digit number 
if (num1 > 999) and (num2 < 10001):
    print(num1, "is a four digit number")
else:
    print(num1, "is not a four digit number")

#enter another value 
num2 = int(input("Enter another number: "))

#which of the two values is the smallest or if they are equal
if num1 > num2: 
    print(num2, "is smaller than", num1)
elif num2 > num1:  
    print(num1, "is smaller than", num2)
elif num1 == num2: 
    print(num1, "equals", num2)

# if the second value is a multiple of the first value 
if num1 % num2 == 0: 
    print(num2, "is a multiple of", num1)
else:
    print(num2, "is not a multiple of", num1)

#if the first value is, or is not a multiple of the second value 
if num2 % num1 == 0: 
    print(num1, "is a multiple of", num2)
else: 
    print(num1, "is not a multiple of", num2)
