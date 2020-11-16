'''
elena corpus
CSCI 161
lab exam

'''

#total number of characters without spaces 
def get_num_of_non_WS_characters(userStr):
    #print("total number of characters:", len(userStr) - userStr.count(' '))
    return len(userStr) - userStr.count(' ')

#total number of words 
def get_num_of_words(userStr):
    words = userStr.split()
    count = 0
    for word in words:
        count = count + 1
    return count
    
#statement written backwards word for word 
def reverse_userStr(userStr):
    reverse = userStr.split()
    reverse.reverse()
    result = ' '.join(reverse)
    return result
    return userStr

def replace_punctuation(userStr):
    #semicolon count and exclamation count 
    exclamationCount = userStr.count("!")
    semicolonCount = userStr.count(";")
    translation = userStr[:]
    translation = translation.replace("!", ".")
    translation = translation.replace(";" , ",")
    #return exclamationCount
    #return semicolonCount
    return translation
    

#printing the menu and choosing what to find until typing q 
def print_menu(userStr):
    print("MENU")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("r - Reserse the order of the words in the sentence")
    print("p - Replace Punctuation")
    print("q - Quit")
    menuOp = input("Choose an option from the menu: ")
    while (menuOp != 'c') and (menuOp !='r' ) and (menuOp != 'w') and (menuOp != 'q') and (menuOp != 'p'):
        print('Enter a valid value')
        menuOp = input("Choose an option from the menu: ")

    if menuOp == 'c':
        print("total number of characters without whitespace:",get_num_of_non_WS_characters(userStr))
    elif menuOp == "w":
        print("total number of words:" , get_num_of_words(userStr))
    elif menuOp == "r":
        print("Reversed Input:",reverse_userStr(userStr))
        print("Originial Input:", userStr)
    elif menuOp == "p":
        print("Punctuation Replaced")
        print("exclamationCount:" , exclamationCount )
        print("semicolonCount:" , semicolonCount)
        print("edited text:" , replace_punctuation(userStr))
    return menuOp, userStr

#Main Code 
userStr = input('Enter a statement or sentence of your choosing: ')
print("You entered: ", userStr)

exclamationCount = userStr.count("!")
semicolonCount = userStr.count(";")

menuOp = 'y'
while menuOp != 'q':
    menuOp, userStr = print_menu(userStr)






