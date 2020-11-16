'''
elena corpus
program 11
csci 161
merge short
'''

def mergeSort(myList):
    if len(myList) > 1:
        #splitting the list 
        mid = len(myList) // 2
        #left half 
        lefthalf = myList[:mid]
        #right half 
        righthalf = myList[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        #comparing lists to decipher which is greater than or less than 
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                myList[k] = lefthalf[i]
                i = i + 1
            else:
                myList[k] = righthalf[j]
                j = j + 1
            k = k + 1
            
        #determining if i from the left side is less than what is in the left side
        while i < len(lefthalf):
            myList[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        #determining if 
        while j < len(righthalf):
            myList[k] = righthalf[j]
            j = j + 1
            k = k + 1

myList = [22, 64, 11, 34, 25, 90, 12]
mergeSort(myList)
print("Sorted:", myList)


