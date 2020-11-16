'''
elena corpus
program 6 
csci 161
'''
#adding a player to the dictionary 
def addPlayer(soccerPlayers):
    jerseyNum = int(input("Enter player's jersey number (0-99): "))
    if int((jerseyNum < 0) or (jerseyNum > 99)):
        jerseyNum = input("enter a different jersey number: ")
    else:
        playerRating = int(input("Enter player's rating (0 - 10): "))
        if int((playerRating < 0) and (playerRating > 10)):
            playerRating = int(input("enter a rating within the range of 0 - 10: "))
        else:
            soccerPlayers[jerseyNum] = playerRating

#removing a player from the dictionary
def removePlayer(soccerPlayers):
    jerseyNum = int(input("enter player's jersey number to remove: "))
    del soccerPlayers[jerseyNum]

#output players about the inputted rating
def outputPlayerAboveRating(soccerPlayers):
    #teamList = [soccerPlayers]
    listOfSoccer = sorted(list(soccerPlayers.keys()))
    rating = int(input("enter a rating: "))
    for i in listOfSoccer:
        if soccerPlayers[i] > rating:
            print('Jersey Number:',i,', Rating:', soccerPlayers[i])


#updating players rating        
def updatePlayerRating(soccerPlayers):
    jerseyNum = int(input("enter player's jersey number to update rating: "))
    playerRating = int(input("enter player's new rating: "))
    soccerPlayers[jerseyNum] = playerRating

#print the roster
def outputRoster(soccerPlayers):
    print("ROSTER")
    for keys, values in soccerPlayers.items():
        print("Jersey Number:", keys,", Rating:", values)

#print the menu
def print_menu(soccerPlayers): 
    print()
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    menuOp = input("Choose an option from the menu: ")
    while (menuOp != 'a') and (menuOp !='d' ) and (menuOp != 'u') and (menuOp != 'r') and (menuOp != 'o') and (menuOp != 'q'):
        print('Enter a valid value')
        menuOp = input("Choose an option from the menu: ")
    if menuOp == 'a':
        addPlayer(soccerPlayers)
    elif menuOp == "d":
        removePlayer(soccerPlayers)
    elif menuOp == "u":
        updatePlayerRating(soccerPlayers)
    elif menuOp == "r":
        outputPlayerAboveRating(soccerPlayers)
    elif menuOp == "o":
        outputRoster(soccerPlayers)
    return menuOp, soccerPlayers

soccerPlayers = {}
teamList = []
#inputting the roster
for inputs in range(0,5):
    jerseyNum = int(input("Enter player's jersey number (0-99): "))
    if int((jerseyNum < 0) or (jerseyNum > 99)):
        jerseyNum = input("enter a different jersey number: ")
    else:
        playerRating = int(input("Enter player's rating (0 - 10): "))
        if int((playerRating < 0) and (playerRating > 10)):
            playerRating = int(input("enter a rating within the range of 0 - 10: "))
        else:
            soccerPlayers[jerseyNum] = playerRating

#printing the roster
print()
print("ROSTER")
for keys, values in soccerPlayers.items():
    print("Jersey Number:", keys,", Rating:", values)


menuOp = 'y'
while menuOp != 'q':
    menuOp, soccerPlayers = print_menu(soccerPlayers)
